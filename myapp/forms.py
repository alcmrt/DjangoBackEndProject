from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    """
    Yeni kullanıcıyı oluşturmak için tarayıcıda gösterilecek olan form alanları ve özellikleri
    """
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class UpdateUserForm(UserChangeForm):
    """
    Kullanıcıyı güncellemek için tarayıcıda gösterilecek olan form alanları ve özellikleri
    """
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Kullanıcı Adı"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ad"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Soyad"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}))

    username.label = "Kullanıcı Adı"
    first_name.label = "Ad"
    last_name.label = "Soyad"
    email.label = "Email Adresi"

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
