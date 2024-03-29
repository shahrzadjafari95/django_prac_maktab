from captcha.fields import CaptchaField
from django import forms

from website.models import Contact, Newsletter


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()  # captcha for contact form

    class Meta:
        model = Contact  # میتوانیم تمام فیلر های داخل مدل را به صورت بک فرم نمایش دهیم
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
