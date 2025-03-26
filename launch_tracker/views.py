from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.sites import requests
import requests
from rest_framework import viewsets
from rest_framework.response import Response


class LaunchViewSet(viewsets.ViewSet):
    def list(self, request):
        response = requests.get("https://api.spacexdata.com/v4/launches")
        return Response(response.json())

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
