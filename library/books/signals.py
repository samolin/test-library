from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Book
from .tasks import send_new_book_notification_email


@receiver(post_save, sender=Book)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        send_new_book_notification_email.delay(instance.title, instance.author)