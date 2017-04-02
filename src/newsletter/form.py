from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not domain == 'gmail':
            raise forms.ValidationError("Please make sure you use gmail ")
        if not extension == "com":
            raise forms.ValidationError("Please make sure you use . com email address")
        return email

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not domain == 'gmail':
            raise forms.ValidationError("Please make sure you use gmail ")
        if not extension == "com":
            raise forms.ValidationError("Please make sure you use . com email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if form.is_valid():
            print form.cleaned_data
        return full_name