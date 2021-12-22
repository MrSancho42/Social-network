from rest_framework import serializers
from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'login', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password:
            instance.set_password(password)
        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'login', 'date_joined', 'last_login', 'last_activity')
        read_only_fields = ('id', 'login', 'date_joined', 'last_login', 'last_activity')
