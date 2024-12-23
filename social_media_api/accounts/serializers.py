from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Get the custom user model
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Define a password field explicitly to ensure proper write-only behavior
    bio = serializers.CharField(required=False, allow_blank=True, max_length=255)
    profile_picture = serializers.ImageField(required=False, allow_null=True)
    password = serializers.CharField(write_only=True)


    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password']
        read_only_fields = ['followers']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Remove the password from validated_data and use `create_user` to hash it properly
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        if password:
            user.set_password(password)  # Hash the password
            user.save()  
        # Create a token for the new user
        Token.objects.create(user=user)
        return user
    
class FollowSerializer(serializers.Serializer):
    """Serializer for managing user follow actions"""
    follower = serializers.CharField(read_only=True)
    following = serializers.CharField()
