from django.contrib import admin

from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
	search_fields = ('title', 'caption',)
	list_filter = ('uploaded', 'photographer', 'status',)
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'uploaded', 'status')
	ordering = ['-uploaded']
	actions = ['make_aggregated']
	readonly_fields = ('width', 'height')

	fieldsets = (
		(None, {
			'fields': ('title', 'slug', 'photo', 'caption', 'photographer', 'one_off_photographer', 'uploaded')
		}),
		('Attributes', {
			'fields': ('width', 'height', 'alt_text', 'external_url',)
		}),
		('Settings', {
			'fields': ('status',)
		}),
	)

admin.site.register(Photo, PhotoAdmin)