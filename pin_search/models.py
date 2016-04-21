from __future__ import unicode_literals

from django.db import models


class PostOfficeDetails(models.Model):
    office_name = models.CharField(max_length=255, null=True, blank=True)
    pin_code = models.CharField(max_length=10, null=True, blank=True)
    office_type = models.CharField(max_length=255, null=True, blank=True)
    delivery_status = models.CharField(max_length=255, null=True, blank=True)
    division = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    circle = models.CharField(max_length=255, null=True, blank=True)
    taluk = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.office_name
