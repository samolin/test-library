from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from time import sleep

from .models import User


@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(pk=user_id)
    sleep(20)
    send_mail(
        'Добро пожаловать!',
        'Здравствуйте {}, добро пожаловать в нашу библиотеку.'.format(user.username),
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )