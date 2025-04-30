from datetime import datetime

import requests
from django.shortcuts import render
from django.utils.timezone import make_aware
from django.views import View
from django.views.generic import TemplateView
from .models import FavoriteLaunch, User


class LaunchListView(TemplateView):
    template_name = "launch_tracker/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get('https://api.spacexdata.com/v4/launches/past')
        launches = response.json()

        context['launches'] = [
            {
                'id': launch['id'],
                'name': launch['name'],
                'date': datetime.fromisoformat(launch['date_utc'].replace('Z', '+00:00')),
                'flight_number': launch['flight_number'],
                'details': launch.get('details'),
                'youtube': f"https://youtu.be/{launch['links']['youtube_id']}" if launch['links'].get(
                    'youtube_id') else None,
                'article': launch['links'].get('article'),
                'wikipedia': launch['links'].get('wikipedia'),
                'image': launch['links']['patch']['small'],
            }
            for launch in launches
        ]
        return context


class FavoritesView(TemplateView):
    template_name = "launch_tracker/favorites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["favorites"] = FavoriteLaunch.objects.filter(user=self.request.user)
        else:
            context["favorites"] = []
        return context


class LoginView(TemplateView):
    template_name = "launch_tracker/login.html"

class LaunchDetailView(View):
    def get(self, request, pk):
        response = requests.get(f"https://api.spacexdata.com/v4/launches/{pk}")
        launch = response.json()
        return render(request, "launch_tracker/page.html", {"launch": launch})
