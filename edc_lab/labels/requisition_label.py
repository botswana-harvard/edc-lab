from django.apps import apps as django_apps
from edc_label import Label
# from edc_registration.models import RegisteredSubject
from arrow.arrow import Arrow
from django.conf import settings


edc_protocol_app_config = django_apps.get_app_config('edc_protocol')


class RequisitionLabel(Label):

    label_template_name = 'requisition'

    def __init__(self, requisition=None, item=None, user=None, label_template_name=None):
        self.label_template_name = label_template_name or self.label_template_name
        super().__init__(label_template_name=self.label_template_name)
        self.item = item or 1
        self.requisition = requisition
        self.user = user
#         self.registered_subject = RegisteredSubject.objects.get(
#             subject_identifier=self.requisition.subject_identifier)
        self.label_name = self.requisition.human_readable_identifier

    @property
    def label_context(self):
        utc = Arrow.fromdatetime(
            self.requisition.drawn_datetime or self.requisition.created)
        dte = utc.to(settings.TIME_ZONE).datetime
        formatted_date = dte.strftime("%Y-%m-%d %H:%M")
        printed = 'PRINTED: ' if not self.requisition.drawn_datetime else 'DRAWN: '
        return {
            'requisition_identifier': self.requisition.requisition_identifier,
            'item': self.item,
            'item_count': self.requisition.item_count or 1,
            'primary': '<P>',
            'barcode_value': self.requisition.requisition_identifier,
            'protocol': edc_protocol_app_config.protocol,
            'site': str(self.requisition.site.id),
            'site_name': str(self.requisition.site.name),
            'clinician_initials': self.user.username[0:2].upper(),
            'drawn_datetime': f'{printed}{formatted_date}',
            'subject_identifier': self.requisition.subject_identifier,
            'gender': 'N/A', #self.registered_subject.gender,
            'dob': 'N/A', #self.registered_subject.dob,
            'initials': 'N/A', #self.registered_subject.initials,
            'alpha_code': self.requisition.panel_object.alpha_code,
            'panel': self.requisition.panel_object.abbreviation}
