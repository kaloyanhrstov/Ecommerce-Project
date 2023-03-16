from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserChangeForm
from django import forms

UserModel = get_user_model()


class CreateUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']


class EditUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': "Email",
                }
            ),
        }
