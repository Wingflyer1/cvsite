from django.contrib import admin
from .models import Certificates
# Register your models here.

class CertificatesAdmin(admin.ModelAdmin):
	list_display = ['certificate', 'comment', 'valid_from', 'valid_to', 'timestamp', 'updated']
	# class Meta:
	# 	model = SignUp



admin.site.register(Certificates, CertificatesAdmin)