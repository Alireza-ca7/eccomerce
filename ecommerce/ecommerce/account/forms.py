from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email address is already in use.")
        if len(email) > 250:
                raise forms.ValidationError("Email address is too long.")
        return email

class LoginForm(AuthenticationForm):
     username= forms.CharField(widget=TextInput())
     password= forms.CharField(widget=PasswordInput())