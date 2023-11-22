"""API URL Configuration"""
from django.urls import path

from .views import DurationApi
from .views import SameActorApi
from .views import PopulateApi
from .views import YearApi


urlpatterns = [
    path("populate", PopulateApi.as_view()),
    path("actor", SameActorApi.as_view()),
    path("duration", DurationApi.as_view()),
    path("year", YearApi.as_view()),
]
