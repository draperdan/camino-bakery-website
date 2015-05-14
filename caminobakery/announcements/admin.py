from django.contrib import admin

from .models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('text', 'link', 'created', 'is_public',)
    list_filter = ('is_public', 'created',)
    list_editable = ('is_public',)
    readonly_fields = ['created']
    fields = (
        'text',
        'link',
        'created',
        'is_public',
    )

admin.site.register(Announcement, AnnouncementAdmin)
