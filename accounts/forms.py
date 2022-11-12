from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomeUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age',)  # or: fields = UserCreationForm.Meta.Fields + ('age")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomeUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age',)  # or: fields = UserCreationForm.Meta.Fields
