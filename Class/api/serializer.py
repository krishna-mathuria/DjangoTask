 
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class StudentSerializer(serializers.ModelSerializer):
    """
    The details for the users in the group Student
    """
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email',]

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for complete details of all the users in the database
    """
    class Meta:
        model = User
        fields = '__all__'