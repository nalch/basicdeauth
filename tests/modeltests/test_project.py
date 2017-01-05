import pytest

from model_mommy import mommy

from nalch_basicdeauth.models import UrlEntry


@pytest.mark.django_db
def test_save():
    urlentry = mommy.make(UrlEntry)
    assert str(urlentry) == urlentry.name
