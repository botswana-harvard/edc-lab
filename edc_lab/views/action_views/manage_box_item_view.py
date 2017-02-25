from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe

from ..mixins import IdentifierDoesNotExist, BoxViewMixin
from .base_action_view import BaseActionView, app_config


class ManageBoxItemView(BoxViewMixin, BaseActionView):

    post_url_name = app_config.manage_box_listboard_url_name
    valid_form_actions = [
        'add_item', 'renumber_items', 'remove_selected_items']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @property
    def url_kwargs(self):
        return {
            'action_name': self.kwargs.get('action_name'),
            'box_identifier': self.box_identifier}

    def process_form_action(self):
        if self.action == 'add_item':
            self.add_box_item()
        elif self.action == 'renumber_items':
            self.renumber_items()
        elif self.action == 'remove_selected_items':
            self.remove_selected_items()

    def remove_selected_items(self):
        if not self.selected_items:
            message = ('Nothing to do. No items have been selected.')
            messages.warning(self.request, message)
        else:
            deleted = self.box_item_model.objects.filter(
                pk__in=self.selected_items).delete()
            message = ('{} items have been removed.'.format(deleted[0]))
            messages.success(self.request, message)

    def renumber_items(self):
        box_items = self.box.boxitem_set.all().order_by('position')
        if box_items.count() == 0:
            message = ('Nothing to do. There are no items in the box.')
            messages.warning(self.request, message)
        else:
            for index, boxitem in enumerate(
                    self.box.boxitem_set.all().order_by('position'), start=1):
                boxitem.position = index
                boxitem.save()
            message = ('Box {} has been renumber. Be sure to physically verify '
                       'the position of each specimen.'.format(
                           self.box_identifier))
            messages.success(self.request, message)

    def add_box_item(self, **kwargs):
        """Adds the item to the next available position in the box.
        """
        try:
            box_item = self.box_item_model.objects.get(
                box__box_identifier=self.box_identifier,
                identifier=self.box_item_identifier)
        except self.box_item_model.DoesNotExist:
            try:
                box_item = self.box_item_model.objects.get(
                    identifier=self.box_item_identifier)
            except self.box_item_model.DoesNotExist:
                box_item = self.box_item_model(
                    box=self.box,
                    identifier=self.box_item_identifier,
                    position=self.box.next_position)
                box_item.save()
            else:
                message = mark_safe(
                    'Item is already packed. See box <a href="{href}" class="alert-link">'
                    '{box_identifier}</a>'.format(
                        href=reverse(
                            self.listboard_url_name,
                            kwargs={
                                'box_identifier': box_item.box.box_identifier,
                                'action_name': 'manage'}),
                        box_identifier=box_item.box.box_identifier))
                messages.error(self.request, message)
        except IdentifierDoesNotExist:
            pass
        else:
            message = 'Duplicate item. {} is already in position {}.'.format(
                box_item.human_readable_identifier, box_item.position)
            messages.error(self.request, message)