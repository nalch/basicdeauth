from django.contrib import admin

from .forms import (
    UrlEntryForm,
)

from .models import (
    UrlEntry,
)


class UrlEntryAdmin(admin.ModelAdmin):
    form = UrlEntryForm

admin.site.register(UrlEntry, UrlEntryAdmin)
