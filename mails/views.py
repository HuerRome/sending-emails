from re import template
from statistics import correlation
from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings 
from django.core.mail import EmailMultiAlternatives

from mails.settings import EMAIL_HOST_USER

def send(mail):
    context = {'mail':mail}
    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba',
        'Codigo Facilito',
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def index(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
         
        send_email(mail)
    

    return render(request, 'index.html', {})
