from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from accountapp.models import User


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['userid'].disabled = True