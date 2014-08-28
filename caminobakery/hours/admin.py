from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('day', 'open_hour', 'close_hour')	

admin.site.register(Schedule, ScheduleAdmin)
