from django.db import models
from datetime import date
# Create your models here.

class Certificates(models.Model):
    certificate = models.CharField(max_length=120, blank=True, null=True)
    comment = models.CharField(default='', max_length=120, blank=True, null=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def is_expired(self):
        present = date.today()
        if present > self.valid_to:
            return True
        return False