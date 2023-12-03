from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from ToDoApp.accounts.models import CustomUser


class ProjectUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
        )


class ProjectUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'photo',
        )
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'photo': 'Photo URL',
        }


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Password',
            }
        )
    )
