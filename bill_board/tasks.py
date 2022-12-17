from datetime import timedelta

from allauth.account.models import EmailAddress
from celery import shared_task

from django.template.loader import render_to_string
from django.utils import timezone

from Board.settings import SITE_LINK
from .utilites import send_mail
from .models import User, Advert, Resp

from kombu.exceptions import OperationalError


@shared_task
def mail_for_add_response(username, email, title, pk):
    """
    Sending email after response added
    """
    adv = Advert.objects.get(id=pk)
    html_content = render_to_string(
        template_name='email/added_response.html',
        context={
            'name': username,
            'title': title,
            'link': SITE_LINK,
            'advert': adv,
            }
    )

    subject = f'{username}, a new response to "{title}" received'
    print(subject)
    try:
        send_mail(email, subject, html_content)
    except OperationalError:
        print('could not send e-mail on a new response')
    return


@shared_task
def mail_for_change_status(username, email, title, pk):
    """
    Sending email after response accepted
    """
    adv = Advert.objects.get(id=pk)
    html_content = render_to_string(
        template_name='email/response_accepted.html',
        context={
            'name': username,
            'title': title,
            'link': SITE_LINK,
            'advert': adv,
        }
    )
    subject = f'{username}, your response has been accepted.'
    try:
        send_mail(email, subject, html_content)
    except OperationalError:
        print('could not send e-mail on response status change')
    return


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

    # checking if there werwe new ads for the last 24 hrs and sending out e-mails
    the_day = timezone.now() - timedelta(days=1)
    adv = Advert.objects.filter(create__gte=the_day)
    for recipient in mailing_list:
        html_content = render_to_string(
            'email/daily_mailing.html',
            {
                'link': SITE_LINK,
                'name': recipient[0],
                'adverts': adv
            }
        )
        try:
            subject = f'{recipient[0]}, please see the daily digest:'
            send_mail(recipient[1], subject, html_content)
        except Exception as e:
            print(f'could not send daily digest for the following reason(s): {e}')
