from django.db import models

# Create your models here.

class Education(models.Model):
    school = models.CharField(max_length=120, blank=True, null=True)
    course = models.CharField(max_length=120, blank=False, null=True)
    year_from = models.DateField()
    year_to = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)