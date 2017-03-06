from django.db import models

# Create your models here.

class HostInfo(models.Model):
    host = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)
    port = models.IntegerField(max_length=6)

