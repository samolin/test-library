from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from users.models import User



@shared_task
def send_new_book_notification_email(book_title, book_author):
    users = User.objects.all()
    to_emails = []
    for user in users:
        if user.email not in to_emails:
            to_emails.append(user.email)
            send_mail(
                'Новое поступление',
                'Здравствуйте, {}! У нас новая книга {} от автора {}'.format(user.username, book_title, book_author),
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
