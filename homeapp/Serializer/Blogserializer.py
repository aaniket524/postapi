from rest_framework import serializers
from homeapp.models import models

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Model
        fields = '__all__'