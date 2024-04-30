from django.contrib import admin

# Register your models here.
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time',
                    'end_time', 'is_free', 'is_active')
    list_filter = ('is_free', 'is_active', 'date')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'
    ordering = ('-date', '-start_time')
    readonly_fields = ('created', 'updated')
    list_per_page = 10
    list_editable = ('is_free', 'is_active')
    actions = ['make_inactive', 'make_active']

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = 'Mark selected events as inactive'

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = 'Mark selected events as active'
