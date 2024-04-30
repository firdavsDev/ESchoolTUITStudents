from django.db.models.signals import post_save
from django.dispatch import receiver


from .alerter import Alerter
from .models import Contact


@receiver(post_save, sender=Contact)
def create_contact(sender, instance, created, **kwargs):
    if created:
        tg_alert = Alerter(bot_token='5799450453:AAHsE9kb4wSwttZwwPXWxmtkVzndTZTC64w',
                           chat_id='-1001759379760')
        tg_alert.custom_alert(
            text=f'New contact: {instance.first_name} {instance.last_name} \n\nMessage: {instance.message}')
