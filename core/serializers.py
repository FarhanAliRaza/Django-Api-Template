from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from accounts.models import User
from core.models import *


# class ModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SomeModel
#         fields = '__all__'
#         #or
#         # exclude = ['id']
#         read_only_fields = ['id']


# class CustomSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     logo = serializers.ImageField()
#     email = serializers.EmailField()
#     def create(self, validated_data):
#         pass
#     def update(self, instance, validated_data):
#         pass


# class SerializerWithMethodFields(serializers.ModelSerializer):
#     name = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Modal
#         fields = ['id',  'name', 'created_at',  ]

#     def get_name(self, obj):
#         name = f"{obj.investor.fname} {obj.investor.lname}"
#         return name
