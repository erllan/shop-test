from rest_framework import serializers
from shop.models import User


class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
