import requests
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FavoriteLaunch
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class FavoriteLaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteLaunch
        fields = '__all__'

# ViewSet to work with SpaceX API
class LaunchViewSet(viewsets.ViewSet):
    BASE_URL = "https://api.spacexdata.com/v4/launches"

    def list(self, request):
        """Getting all the launches"""
        response = requests.get(self.BASE_URL)
        return Response(response.json())

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        user = request.user
        FavoriteLaunch.objects.create(user=user, launch_id=pk)
        return Response({"message": "Launch added to favorites"})
