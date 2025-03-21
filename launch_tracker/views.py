from django.contrib.sites import requests
import requests
from rest_framework import viewsets
from rest_framework.response import Response


class LaunchViewSet(viewsets.ViewSet):
    def list(self, request):
        response = requests.get("https://api.spacexdata.com/v4/launches")
        return Response(response.json())
