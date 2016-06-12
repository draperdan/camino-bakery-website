from django.contrib import admin

from .models import Special


class SpecialAdmin(admin.ModelAdmin):
    list_display = ('description', 'day_offered')
    list_filter = ['day_offered']

admin.site.register(Special, SpecialAdmin)
