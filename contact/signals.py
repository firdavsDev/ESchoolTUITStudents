from django.db.models.signals import post_save
from django.dispatch import receiver


from .alerter import Alerter
from .models import Contact


@receiver(post_save, sender=Contact)
def create_contact(sender, instance, created, **kwargs):
    if created:
        tg_alert = Alerter(bot_token='6807947321:AAHoCa_ny3PdGOjKgm-v2s9MkcrMBDRIwv8',
                           chat_id='-1002032242624')
        tg_alert.custom_alert(
            text=f'New contact: {instance.first_name} {instance.last_name} \n\nMessage: {instance.message}')
