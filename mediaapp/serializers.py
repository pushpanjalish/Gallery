from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Gallery

class Imgserializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields='__all__'