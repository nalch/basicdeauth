import pytest

from model_mommy import mommy

from nalch_caldav2ical.models import CalendarEntry


@pytest.mark.django_db
def test_save():
    calendar_entry = mommy.make(CalendarEntry)
    assert str(calendar_entry) == calendar_entry.name
