import json

from django.db import models
import json


# Create your models here.
class Region(models.Model):
    env = models.CharField(max_length=255)
    envName = models.CharField(max_length=255)
    enterprise = models.CharField(max_length=255)
    enterpriseName = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    accountName = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    regionName = models.CharField(max_length=255)
    projectId = models.CharField(max_length=255, blank=True)
    cloudProvider = models.CharField(max_length=255, blank=True)
    cloudCode = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.env + self.account + self.region + self.projectId
