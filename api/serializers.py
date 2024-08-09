#from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, User #Note

'''class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            role=validated_data.get("role", User.CUSTOMER)  # Default to CUSTOMER if role not provided
        )
        return user'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data): 
        user = User(
            username=validated_data["username"],
            role=validated_data.get("role", User.CUSTOMER)  # Default to CUSTOMER if role not provided
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    
'''class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author":{"read_only": True}}'''

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "category", "posted_at"]

