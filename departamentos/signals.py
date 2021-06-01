from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from departamentos.models import Depto


@receiver(post_save, sender=User, dispatch_uid='save_new_depto')
def save_Depto(sender, instance, created, **kwargs):
    if created:
        depto = Depto(user=instance)
        depto.save()
