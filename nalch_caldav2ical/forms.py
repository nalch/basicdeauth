from django.forms import ModelForm, PasswordInput

from .models import (
    CalendarEntry,
)


class CalendarEntryForm(ModelForm):
    class Meta:
        model = CalendarEntry
        widgets = {
            'password': PasswordInput(),
        }
