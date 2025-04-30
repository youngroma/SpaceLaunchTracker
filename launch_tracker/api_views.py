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
