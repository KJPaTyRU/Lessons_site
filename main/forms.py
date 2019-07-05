from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255)
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput)

