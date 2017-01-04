from django.contrib import admin

from .forms import (
    CalendarEntryForm,
)

from .models import (
    CalendarEntry,
)


class CalendarEntryAdmin(admin.ModelAdmin):
    form = CalendarEntryForm

admin.site.register(CalendarEntry, CalendarEntryAdmin)
