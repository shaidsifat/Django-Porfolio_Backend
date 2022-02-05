from django.contrib import admin
from django.urls import path
from .views import Contact
urlpatterns = [
    path('polls/',Contact.as_view(),name="Contact"),
]
