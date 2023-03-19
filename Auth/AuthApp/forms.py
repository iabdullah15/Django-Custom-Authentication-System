from django import forms

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'mobile_no']


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:

        model = CustomUser
        fields = ['email']