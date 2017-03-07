from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_dashboard.model_mixins import SearchSlugModelMixin, SearchSlugManager

from ...managers import ManifestManager
from ...model_mixins.shipping import ManifestModelMixin
from .consignee import Consignee
from .shipper import Shipper


class Manager(ManifestManager, SearchSlugManager):
    pass


class Manifest(ManifestModelMixin, SearchSlugModelMixin, BaseUuidModel):

    consignee = models.ForeignKey(
        Consignee,
        verbose_name='Consignee',
        on_delete=PROTECT)

    shipper = models.ForeignKey(
        Shipper,
        verbose_name='Shipper/Exporter',
        on_delete=PROTECT)

    objects = Manager()

    history = HistoricalRecords()

    def __str__(self):
        return '{} created on {} by {}'.format(
            self.manifest_identifier,
            self.manifest_datetime.strftime('%Y-%m-%d'),
            self.user_created)

    @property
    def count(self):
        return self.manifestitem_set.all().count()

    def get_slugs(self):
        slugs = [
            self.manifest_identifier,
            self.human_readable_identifier,
            self.shipper.name,
            self.consignee.name]
        return slugs

    class Meta(ManifestModelMixin.Meta):
        app_label = 'edc_lab'