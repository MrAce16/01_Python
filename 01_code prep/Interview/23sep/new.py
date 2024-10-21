from django.db import models
from rest_framework import serializers
from rest_framework import viewsets


# post

Class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

Class PostSerializer(serializers.Modelserializer):
    
    class Data:
        model = post
        field = '__all__'

class PostViewsets(viewsets.ModelViewSet):
    query = post.objects.all()
    serializerst


