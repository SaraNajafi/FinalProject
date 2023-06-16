from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(UserCreationForm):
        email = forms.EmailField(required=True)

        class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2')

        def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')

            if email and User.objects.filter(email=email).exclude(username=username).count():
                raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
            return email

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user