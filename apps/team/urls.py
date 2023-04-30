from django.urls import path
from .views import TeamListAPIView


urlpatterns = [
    path('top_teams/', TeamListAPIView.as_view()),
]