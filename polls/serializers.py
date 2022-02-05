from django.db.models import fields
from rest_framework import serializers

from .models import Contact

class Book_Doctor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
