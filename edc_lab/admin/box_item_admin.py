from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, audit_fields

from ..admin_site import edc_lab_admin
from ..forms import BoxItemForm
from ..models import BoxItem
from .base_model_admin import BaseModelAdmin


@admin.register(BoxItem, site=edc_lab_admin)
class BoxItemAdmin(BaseModelAdmin, admin.ModelAdmin):

    form = BoxItemForm

    fieldsets = (
        (None, {
            'fields': (
                'box',
                'position',
                'identifier',
                'comment')}),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj=obj) + audit_fields

    list_display = ('identifier', 'position', )
