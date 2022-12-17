from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from allauth.account.signals import email_confirmed
from django.shortcuts import get_object_or_404

from .models import Resp, Advert
from .tasks import mail_for_add_response, mail_for_change_status

from kombu.exceptions import OperationalError


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    # Once e-mail is verified, the user is activated and assigned staff (needed for uploading files to ckeditor)

    user = User.objects.get(email=email_address.email)
    user.is_staff = True
    user.is_active = True
    user.save()


@receiver(post_save, sender=Resp)
def add_response(sender, instance, created, *args, **kwargs):
    # Adding the task to send email on response received
    if created:
        adv = get_object_or_404(Advert, pk=instance.post_id)
        try:
            mail_for_add_response.apply_async(
                (adv.author.username, adv.author.email, adv.title, adv.id),
                countdown=20,
            )
            print(f'title from signals: {adv.title}')
        except OperationalError as e:
            print(f'could not send email, this is why: {e}')

    # Adding the task to send email on response accepted
    elif kwargs.get('update_fields'):
        try:
            mail_for_change_status.apply_async(
                (instance.author.username, instance.author.email, instance.post.title, instance.post.id),
                countdown=20,
            )
        except OperationalError as e:
            print(f'could not send email, this is why: {e}')
    return
