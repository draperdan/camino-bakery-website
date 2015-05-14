from django.contrib import admin

from news.models import Story
from media.models import Photo


class StoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    filter_horizontal = ('categories',)
    list_display = ('headline', 'pub_date', 'status')
    list_display_links = ('headline',)
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('headline',)}
    search_fields = ('headline',)
    actions = ('make_selected_Stories_live', 'make_selected_Stories_draft')

    fieldsets = (
        ('Metadata', {
            'fields': ('author', 'pub_date', 'headline', 'slug', 'status',)
        }),
        (None, {
            'fields': ('excerpt', 'body',)
        }),
        (None, {
            'fields': ('categories',)
        }),
        (None, {
            'fields': ('lead_photo',)
        }),
    )

    def make_selected_Stories_live(self, request, queryset):
        rows_updated = queryset.update(status=1)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as live." % message_bit)

    def make_selected_Stories_draft(self, request, queryset):
        rows_updated = queryset.update(status=2)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as draft." % message_bit)

admin.site.register(Story, StoryAdmin)
