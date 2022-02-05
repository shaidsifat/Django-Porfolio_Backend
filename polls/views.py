from django.shortcuts import render

# Create your views here.
from .models import Contact
from django.contrib.auth.models import User
from polls.serializers import Book_Doctor_Serializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class Contact(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class =  Book_Doctor_Serializer
    
