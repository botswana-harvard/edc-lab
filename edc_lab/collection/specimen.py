import re

from django.apps import apps as django_apps

from edc_constants.constants import YES, NO

from edc_lab.aliquot.aliquot import Aliquot

app_config = django_apps.get_app_config('edc_lab')
edc_protocol_app_config = django_apps.get_app_config('edc_protocol')


class SpecimenError(Exception):
    pass


class Specimen:

    def __init__(self, requisition, create_primary=None):
        self._aliquots = None
        self.primary_aliquot = None
        self.requisition = requisition
        if not re.match('\d+', self.requisition.specimen_type, re.ASCII):
            raise SpecimenError(
                'Invalid specimen type format. Expected a numeric code. Got {}'.format(self.requisition.specimen_type))
        create_primary = True if create_primary is None else create_primary
        self.get_or_create_primary(create_primary)

    @property
    def aliquots(self):
        """Returns a queryset of aliquots."""
        if not self._aliquots:
            self._aliquots = [Aliquot(obj) for obj in app_config.aliquot_model.objects.filter(
                specimen_identifier=self.specimen_identifier)]
        return self._aliquots

    @property
    def aliquot_count(self):
        return len(self.aliquots)

    def get_or_create_primary(self, create):
        """Gets or creates the primary aliquot."""
        if self.specimen_identifier:
            self.requisition.specimen_identifier = self.specimen_identifier
            try:
                primary_aliquot = app_config.aliquot_model.objects.get(
                    specimen_identifier=self.specimen_identifier,
                    is_primary=True)
            except app_config.aliquot_model.DoesNotExist:
                if create:
                    primary_aliquot = app_config.aliquot_model.objects.create(
                        specimen_identifier=self.specimen_identifier,
                        aliquot_type=self.requisition.specimen_type,
                        aliquot_identifier=self.primary_aliquot_identifier,
                        count=0,
                        medium_count=self.requisition.item_count,
                        medium=self.requisition.item_type,
                        is_primary=True)
            self.primary_aliquot = Aliquot(primary_aliquot)

    @property
    def primary_aliquot_identifier(self):
        return self.specimen_identifier + '0000' + self.requisition.specimen_type + '01'

    @property
    def specimen_identifier(self):
        """Returns a specimen identifier based on the requisition."""
        specimen_identifier = None
        if self.requisition.is_drawn == YES:
            specimen_identifier = '{protocol_number}{requisition_identifier}'.format(
                protocol_number=edc_protocol_app_config.protocol_number,
                requisition_identifier=self.requisition.requisition_identifier)
            if len(specimen_identifier) != (18 - 8):
                raise SpecimenError('Invalid specimen identifier length. Got {}'.format(len(specimen_identifier)))
        return specimen_identifier