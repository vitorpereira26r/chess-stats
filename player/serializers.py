from rest_framework import serializers
from .models import PlayerRequests


class PlayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRequests
        fields = '__all__'