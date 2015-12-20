from django.contrib import admin
from .forms import ExperienceForm
from .models import Experience
# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
	list_display = ['employer', 'position', 'chores', 'year_from', 'year_to', 'timestamp', 'updated']
	form = ExperienceForm
	# class Meta:
	# 	model = SignUp


admin.site.register(Experience, ExperienceAdmin)