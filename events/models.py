from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    title = models.CharField(_('title'), max_length=200)
    description = models.TextField(_('description'))
    date = models.DateTimeField(_('date'))  # date and time
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    is_free = models.BooleanField(_('is free'), default=False)
    location = models.CharField(
        _('location'), max_length=200, blank=True, null=True)
    image = models.ImageField(
        _('image'), upload_to='events/', blank=True, null=True)
    # common fields
    is_active = models.BooleanField(_('is active'), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
