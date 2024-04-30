from django.db import models
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    profile_picture = models.ImageField(
        _('Teacher Picture'), upload_to='teachers/', blank=True, null=True)
    email = models.EmailField(_('email'), max_length=100)
    tg_username = models.CharField(
        _('telegram username with @'), max_length=100)
    phone = models.CharField(_('phone'), max_length=15)
    address = models.CharField(_('address'), max_length=200)
    profession = models.CharField(_('profession'), max_length=100)
    date_of_birth = models.DateField(_('date of birth'))
    bio = models.TextField(_('bio'))
    # common fields
    is_active = models.BooleanField(_('is active'), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')
        ordering = ('-created',)
