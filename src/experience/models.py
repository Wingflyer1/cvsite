from django.db import models
from datetime import datetime

# Create your models here.

class Experience(models.Model):
    employer = models.CharField(max_length=120, blank=True, null=True)
    position = models.CharField(max_length=120, blank=False, null=True)
    chores = models.TextField(blank=False, null=True)
    year_from = models.DateField()
    year_to = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)