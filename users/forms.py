from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from users.models import Role

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    role = forms.ChoiceField(choices=Role.choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial')
        user = initial.get('user') if initial else None
        if not user or not user.is_staff:
            self.fields['role'].widget = forms.HiddenInput()
            self.fields['role'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'CUSTOMER'
        if commit:
            user.save()
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

