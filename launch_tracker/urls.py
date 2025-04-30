from django.urls import path
from .views import LaunchListView, LoginView, FavoritesView, LaunchDetailView

urlpatterns = [
    path('', LaunchListView.as_view(), name="index"),
    path('favorites/', FavoritesView.as_view(), name="favorites"),
    path('login/', LoginView.as_view(), name="login"),
    path('launch/<str:pk>/', LaunchDetailView.as_view(), name="page")
]