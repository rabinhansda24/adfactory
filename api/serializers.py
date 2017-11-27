from home.models import *
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogDetails
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdDetails
        fields = '__all__'