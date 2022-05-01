from django.shortcuts import render
from .forms import SendEmailForm
from django.conf import settings
from django.core.mail import send_mail



def send_email(request):
    form = SendEmailForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        send_mail(
            form.cleaned_data['subject'], 
            form.cleaned_data['body'], 
            settings.EMAIL_HOST_USER, 
            [form.cleaned_data['email']]
        )

    context = {
        'form': form
    }
    return render(request, 'send_email.html', context)
