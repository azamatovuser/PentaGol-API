from django.urls import path
from .views import ArticleAllListAPIView, ArticleLastListAPIView, ArticleRetrieveAPIView, ArticleLastFourListAPIView


urlpatterns = [
    path('list_all/', ArticleAllListAPIView.as_view()),
    path('list_last/', ArticleLastListAPIView.as_view()),
    path('list_last_four/', ArticleLastFourListAPIView.as_view()),
    path('detail/<int:pk>/', ArticleRetrieveAPIView.as_view()),
]