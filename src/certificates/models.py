from django.db import models

# Create your models here.

class Certificates(models.Model):
    certificate = models.CharField(max_length=120, blank=True, null=True)
    comment = models.CharField(default='', max_length=120, blank=True, null=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)