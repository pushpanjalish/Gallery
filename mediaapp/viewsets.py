from operator import mod
from turtle import mode
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

class ImgViewset(viewsets.ModelViewSet):
    queryset=models.Gallery.objects.all()
    serializer_class=serializers.Imgserializer
    parser_classes = (MultiPartParser, FormParser)
    

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)