from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our API"""
    name = serializers.CharField(max_length = 10)

class UserProfileSerializer(serializers.ModelSerializer):
    "A Serializer is for our user profile"
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}
    def create(self,validate_data):
        "Create and Return new user"
        user = models.UserProfile(email= validate_data['email'],name = validate_data['name'])
        user.set_password(validate_data['password'])
        user.save()
        return user
