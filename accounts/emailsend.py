import sys 
sys.path.append('..')

import  django
import os
os.environ["DJANGO_SETTINGS_MODULE"] = 'app.settings'
django.setup()
import requests
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from accounts.models import User
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator


# user = User.objects.get(slug='farhanmyslug')
# x = urlsafe_base64_encode(force_bytes(user.slug))
# tkn = default_token_generator.make_token(user)
# print(default_token_generator.check_token(user, tkn))

# print(x)
# print(force_text(urlsafe_base64_decode(x)))
activation_link = "siteurl"
def email_send(useremail, username, activation_link):

    subject = "site - User Activation Mail"
    html_message = render_to_string('mail_verification.html', {'username': username, 'activation_link' : activation_link})
    plain_message = strip_tags(html_message)
    from_email = 'site <noreply@site.url>'
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to = [useremail, ],
        bcc= []

)
    email.content_subtype = "html"
    try:
        email.send(fail_silently=False)
    except:
        email_send(useremail, username, activation_link)



def email_forgot_send(useremail, username, activation_link):

    subject = "site - Password Reset Email"
    html_message = render_to_string('forgotpassmail.html', {'username': username, 'activation_link' : activation_link})
    plain_message = strip_tags(html_message)
    from_email = 'site <noreply@site.url>'
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to = [useremail, ],

    )
    email.content_subtype = "html"
    try:
        print(email.send(fail_silently=False))
    except Exception as e:
        print(e)
        email_send(useremail, username, activation_link)
