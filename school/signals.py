from django.db.models.signals import pre_save
from django.dispatch import receiver

from school.models import Student


@receiver(pre_save, sender=Student)
def my_callback(sender, instance, **kwargs):
    if instance.phone_number.is_valid():
        # instance.admission_year = "2008"
        print(f"Model saved! Sender was {sender} kwargs {kwargs}")
