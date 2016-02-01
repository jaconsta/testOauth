from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework import serializers

from .models import Enthusiast

class EnthusiastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enthusiast
        fields = ('city', )


class UserSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='enthusiast.city')  # EnthusiastSerializer(many=False)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'city')

    def create(self, validated_data):
        enthusiast_data = validated_data.pop('enthusiast')
        validated_data['password'] = get_random_string()
        user = User.objects._create_user(**validated_data)

        enthusiast = Enthusiast.objects.create(user=user, **enthusiast_data)
        return user

