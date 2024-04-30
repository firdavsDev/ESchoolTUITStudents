from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from teachers.models import Teacher


class Course(models.Model):
    title = models.CharField(_('title'), max_length=100, unique=True, db_index=True, help_text=_(
        'The title of the course.'), blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='courses', verbose_name=_('teacher'), blank=True, null=True)
    picture = models.ImageField(
        _('Course Picture'), upload_to='courses/', blank=True, null=True)
    is_free = models.BooleanField(_('is free'), default=True)
    rank = models.IntegerField(_('rank'), default=0, help_text=_(
        'The higher the number, the higher the rank'), validators=[MinValueValidator(0), MaxValueValidator(5)])
    duration = models.PositiveIntegerField(
        _('duration'), help_text=_('Duration in days'), default=0)
    enrolled_students = models.PositiveIntegerField(
        _('enrolled students'), default=0)
    price = models.DecimalField(
        _('price'), max_digits=6, decimal_places=2, default=0.00)
    start_date = models.DateField(_('start date'), blank=True, null=True)
    end_date = models.DateField(_('end date'), blank=True, null=True)
    # common fields
    is_active = models.BooleanField(_('is active'), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ('-created',)
