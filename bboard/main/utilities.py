from django.template.loader import render_to_string
from django.core.signing import Signer
from datetime import datetime
from os.path import splitext

from bboard.settings import ALLOWED_HOSTS

signer = Signer()


def send_activation_notification(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://locolhost:8000'
    context = {'user': user, 'host': host, 'sigh': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)


def get_timestamp_path(instance, filemame):
    return "%S%S" % (datetime.now().timestamp(), splitext(filemame)[1])