import pytest
import strawberry_django
from strawberry_django.filters import DummyDjangoFilters


@pytest.fixture
def django_filters_mock(mocker):
    return mocker.patch('strawberry_django.filters.django_filters', DummyDjangoFilters())


def test_filter_with_dummy_filters_raises_error(django_filters_mock):
    with pytest.raises(ModuleNotFoundError):
        strawberry_django.filter()


def test_apply_filter_with_dummy_filters_raises_error(django_filters_mock):
    with pytest.raises(ModuleNotFoundError):
        strawberry_django.apply_filter()


def test_get_filter_field_type_with_dummy_filters_raises_error(django_filters_mock):
    with pytest.raises(ModuleNotFoundError):
        strawberry_django.get_filter_field_type()


def test_set_filter_field_type_with_dummy_filters_raises_error(django_filters_mock):
    with pytest.raises(ModuleNotFoundError):
        strawberry_django.set_filter_field_type()
