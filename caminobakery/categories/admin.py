from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
    search_fields = ('title', 'description')
    readonly_fields = ('lead_image_width', 'lead_image_height')

admin.site.register(Category, CategoryAdmin)
