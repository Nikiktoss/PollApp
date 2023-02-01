from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import *


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Username",
                               widget=forms.TextInput(attrs={'class': 'input__field'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'input__field'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'input__field'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'input__field'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')

        validate_password(password=password1)
