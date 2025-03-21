from rest_framework import serializers
from launch_tracker.models import FavoriteLaunch


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteLaunch
        fields = '__all__'