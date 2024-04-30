from django.contrib import admin

# Register your models here.
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'is_free', 'rank', 'duration', 'enrolled_students',
                    'price', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_free', 'is_active')
    search_fields = ('title', 'description')
    date_hierarchy = 'created'
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'teacher', 'picture')
        }),
        ('Course Details', {
            'fields': ('is_free', 'rank', 'duration', 'enrolled_students', 'price', 'start_date', 'end_date')
        }),
        ('Common Fields', {
            'fields': ('is_active', 'created', 'updated')
        }),
    )
