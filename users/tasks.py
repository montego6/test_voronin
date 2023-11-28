from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_letter(email, username):
    send_mail(
        'Welcome to books club',
        f'Welcome to books club, dear {username}',
        None,
        [email],
        fail_silently=False
    )