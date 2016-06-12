from django.contrib import admin

from .models import Item, Size, ItemType, ItemTypeGroup, BreadSchedule


class BreadScheduleAdmin(admin.ModelAdmin):
    list_filter = ('days_available',)


class SizeInline(admin.TabularInline):
    model = ItemType.size.through
    verbose_name = "Size"
    verbose_name_plural = "Sizes"


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'description', 'status', 'is_available')
    search_fields = ('name', 'description')
    list_filter = ('item_type', 'is_seasonal', 'is_available',)
    actions = ('make_selected_Items_live', 'make_selected_Items_draft')
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'status',
                       'one_off_price')
        }),
        ('Photo', {
            'fields': ('photo', 'width', 'height')
        }),
        ('Categorization', {
            'fields': ('item_type',)
        }),
        ('Additional classification', {
            'classes': ('collapse',),
            'fields': ('is_flourless', 'is_vegan', 'is_seasonal',
                       'is_available', 'vegan_option_available',
                       'flourless_option_available')
        }),
    )

    def make_selected_Items_live(self, request, queryset):
        rows_updated = queryset.update(status=1)
        if rows_updated == 1:
            message_bit = "1 item was"
        else:
            message_bit = "%s items were" % rows_updated
        self.message_user(
            request, "%s successfully marked as live." % message_bit)

    def make_selected_Items_draft(self, request, queryset):
        rows_updated = queryset.update(status=2)
        if rows_updated == 1:
            message_bit = "1 item was"
        else:
            message_bit = "%s items were" % rows_updated
        self.message_user(
            request, "%s successfully marked as draft." % message_bit)


class SizeAdmin(admin.ModelAdmin):
    fields = ('size', 'price', 'description')
    list_display = ('size', 'price', 'description')


class ItemTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug',)
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'lead_image',
                       'lead_image_width', 'lead_image_height')
        }),
    )
    inlines = [
        SizeInline,
    ]
    exclude = ('size',)


class ItemTypeGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'description', 'item_types', 'lead_image',
              'lead_image_width', 'lead_image_height')
    list_display = ('title', 'description',)

admin.site.register(BreadSchedule, BreadScheduleAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(ItemTypeGroup, ItemTypeGroupAdmin)
