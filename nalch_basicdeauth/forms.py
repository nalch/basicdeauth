from django.forms import ModelForm, PasswordInput

from .models import (
    UrlEntry,
)


class UrlEntryForm(ModelForm):
    class Meta:
        exclude = ()
        model = UrlEntry
        widgets = {
            'password': PasswordInput(),
        }
