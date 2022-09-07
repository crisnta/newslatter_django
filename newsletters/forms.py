from django import forms
from .models import Newsletter, NewsletterUser

class NewsLetterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']

class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'subject', 'body', 'email', 'status']