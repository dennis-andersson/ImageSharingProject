from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "signup-input", "placeholder": "Username"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "signup-input", "placeholder": "First name"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "signup-input", "placeholder": "Last name"}))
    email = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={"class": "signup-input", "placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        existing_user = User.objects.filter(email=email)
        if existing_user.exists():
            raise forms.ValidationError("A user with this email already exists")

        return email
