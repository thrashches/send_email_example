from django import forms


class SendEmailForm(forms.Form):
    email = forms.EmailField(label='Адрес получателя:')
    subject = forms.CharField(max_length=255, label='Тема письма:')
    body = forms.CharField(widget=forms.Textarea, label='Текст письма:')
