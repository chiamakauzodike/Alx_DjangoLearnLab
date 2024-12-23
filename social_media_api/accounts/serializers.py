from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Define a password field explicitly to ensure proper write-only behavior
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password']
        read_only_fields = ['followers']

    def create(self, validated_data):
        # Remove the password from validated_data and use `create_user` to hash it properly
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()

        # Create a token for the new user
        Token.objects.create(user=user)

        return user
