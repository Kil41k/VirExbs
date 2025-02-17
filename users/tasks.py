from celery import shared_task
from django.core.mail import send_mail
from django.urls import reverse
from .models import User, EmailVerification


@shared_task
def send_email_verification(user_id, mail_id):
    user = User.objects.get(id=user_id)
    mail = EmailVerification.objects.get(id=mail_id)
    send_mail(
        subject='Confirm your account',
        message=f'Confirm your account: http://127.0.0.1:8000{reverse("users:verify", kwargs={"token": mail.token})}',
        from_email='tuglukov.7.diyas@gmail.com',
        recipient_list=[user.email],
        fail_silently=False
    )