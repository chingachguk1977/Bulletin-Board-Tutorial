from datetime import timedelta

from allauth.account.models import EmailAddress
from celery import shared_task

from django.template.loader import render_to_string
from django.utils import timezone

from Board.settings import SITE_LINK
from .utilites import send_mail
from .models import User, Advert


@shared_task
def mail_for_add_response(username, email, title):
    """
    Sending email after response added
    """
    html_content = render_to_string(
        'email/added_response.html',
        {
            'name': username,
            'title': title,
        }
    )

    subject = f'{username}, a new response to "{title}" received.'
    send_mail(email, subject, html_content)
    # return


@shared_task
def mail_for_change_status(username, email):
    """
    Sending email after response accepted
    """
    html_content = render_to_string(
        'email/response_accepted.html',
        {
            'name': username,
        }
    )
    subject = f'{username}, your response has been accepted.'
    send_mail(email, subject, html_content)
    # return


@shared_task
def periodic_mailing():
    """
    daily mailing of news
    """

    # mailing list of verified emails
    mailing_list = []
    users = User.objects.all()
    emails = EmailAddress.objects.filter(verified=True).values_list('user_id', 'email')
    for id, email in emails:
        username = users.get(pk=id).username
        mailing_list.append((username, email))
    mailing_list = list(set(mailing_list))

    # Проверяем наличие объявлений за прошедшие сутки и отправляем письма
    the_day = timezone.now() - timedelta(days=1)
    adv = Advert.objects.filter(create__gte=the_day)
    if adv.exists():
        for recipient in mailing_list:
            html_content = render_to_string(
                'email/daily_mailing.html',
                {
                    'link': SITE_LINK,
                    'name': recipient[0],
                    'adverts': adv
                }
            )
            subject = f'{recipient[0]}, please see the update for the last 24 hours:'
            send_mail(recipient[1], subject, html_content)
