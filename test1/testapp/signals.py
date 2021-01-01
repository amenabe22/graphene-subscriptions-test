from .models import Testmodel
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import tSaveHandler

@receiver(post_save, sender=Testmodel)
def save_testm(sender, instance, **kwargs):
    tSaveHandler(instance)
    print("HEYY", instance)
