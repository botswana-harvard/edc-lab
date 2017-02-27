from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model.models import BaseUuidModel
from edc_dashboard.model_mixins import SearchSlugModelMixin, SearchSlugManager

from ..model_mixins.shipping import VerifyModelMixin
from .manifest import Manifest


class ManifestItemManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, position, identifier, box_identifier):
        return self.get(
            position=position,
            identifier=identifier,
            box_identifier=box_identifier)


class ManifestItem(SearchSlugModelMixin, VerifyModelMixin, BaseUuidModel):

    manifest = models.ForeignKey(Manifest, on_delete=PROTECT)

    identifier = models.CharField(
        max_length=25)

    comment = models.CharField(
        max_length=25,
        null=True,
        blank=True)

    objects = ManifestItemManager()

    def natural_key(self):
        return (self.identifier, ) + self.manifest.natural_key()

    @property
    def human_readable_identifier(self):
        x = self.identifier
        return '{}-{}-{}'.format(x[0:4], x[4:8], x[8:12])

    def get_slugs(self):
        slugs = [self.identifier, self.human_readable_identifier]
        return slugs

    class Meta:
        app_label = 'edc_lab'
        ordering = ('created', )
        unique_together = ('manifest', 'identifier')
