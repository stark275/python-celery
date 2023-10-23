from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import connection
from .models import Student


@receiver(pre_save, sender=Student)
def pre_save_handler(sender, instance, *args, **kwargs):
    # Ici, vous pouvez inspecter l'instance qui est sur le point d'être enregistrée
    
    print(" ---------- SIGNAL OUT-----------")
  
