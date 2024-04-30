from django.contrib import admin

# Register your models here.
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'tg_username', 'phone',
                    'profession', 'date_of_birth', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'email',
                     'tg_username', 'phone', 'profession')
    date_hierarchy = 'created'
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'profile_picture')
        }),
        ('Contact Information', {
            'fields': ('email', 'tg_username', 'phone', 'address')
        }),
        ('Additional Information', {
            'fields': ('profession', 'date_of_birth', 'bio')
        }),
        ('Common Fields', {
            'fields': ('is_active', 'created', 'updated')
        }),
    )
