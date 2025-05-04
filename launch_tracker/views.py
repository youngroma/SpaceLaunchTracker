from datetime import datetime
import requests
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import FavoriteLaunch, User


class LaunchListView(TemplateView):
    template_name = "launch_tracker/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        sort_option = request.GET.get('sort_by', 'date-desc')

        response = requests.get('https://api.spacexdata.com/v4/launches/past')
        launches_raw = response.json()

        launches = []
        for launch in launches_raw:
            try:
                parsed_date = datetime.fromisoformat(launch['date_utc'].replace('Z', '+00:00'))
            except (KeyError, ValueError):
                continue

            launches.append({
                'id': launch['id'],
                'name': launch['name'],
                'date': parsed_date,
                'flight_number': launch.get('flight_number'),
                'details': launch.get('details'),
                'youtube': f"https://youtu.be/{launch['links'].get('youtube_id')}" if launch['links'].get(
                    'youtube_id') else None,
                'article': launch['links'].get('article'),
                'wikipedia': launch['links'].get('wikipedia'),
                'image': launch['links']['patch']['small'],
            })

        if sort_option == 'name-asc':
            launches.sort(key=lambda x: x['name'])
        elif sort_option == 'name-desc':
            launches.sort(key=lambda x: x['name'], reverse=True)
        elif sort_option == 'date-asc':
            launches.sort(key=lambda x: x['date'])
        elif sort_option == 'date-desc':
            launches.sort(key=lambda x: x['date'], reverse=True)

        context['launches'] = launches
        context['sort_option'] = sort_option
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


class LaunchDetailView(View):
    def get(self, request, pk):
        response = requests.get(f"https://api.spacexdata.com/v4/launches/{pk}")
        launch = response.json()
        return render(request, "launch_tracker/page.html", {"launch": launch})
