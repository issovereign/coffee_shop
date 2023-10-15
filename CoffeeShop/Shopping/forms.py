from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label="姓名",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    accountname = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    address = forms.CharField(
        label="地址",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    number = forms.CharField(
        max_length=11,
        label = "電話",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'accountname', 'email', 'address', 'number', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        label = "帳號",
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        label = "密碼",
        widget = forms.PasswordInput(attrs={'class': 'form-control'})
    )