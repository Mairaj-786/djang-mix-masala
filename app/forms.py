from django.contrib.auth.models import User
from django import forms
from .models import Plot,Answer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "Password"}))
    class Meta:
        model = User
        fields = ["username", "password"]

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "Confirm Password"}))
    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]


class PlotForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "title"}))
    desc = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "desc"}))
    class Meta:
        model = Plot
        fields = ["title", "desc"]


class Change_Password(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "Old Password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "New Password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "Confirm "}))
    class Meta:
        model = Plot
        fields = ["old_password", "new_password1","new_password2"]

