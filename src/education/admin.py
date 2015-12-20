from django.contrib import admin
from .forms import EducationForm
from .models import Education
# Register your models here.

class EducationAdmin(admin.ModelAdmin):
	list_display = ['school', 'course', 'year_from', 'year_to', 'timestamp', 'updated']
	form = EducationForm
	# class Meta:
	# 	model = SignUp



admin.site.register(Education, EducationAdmin)