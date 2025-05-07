from django.urls import path
from .views import LaunchListView, FavoritesView, LaunchDetailView, AddToFavoritesView
from .auth_views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path('', LaunchListView.as_view(), name="index"),
    path('favorites/', FavoritesView.as_view(), name="favorites"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('launch/<str:pk>/', LaunchDetailView.as_view(), name="page"),
    path("launch/<str:launch_id>/add/", AddToFavoritesView.as_view(), name="add_to_favorites"),
]