from django.urls import path
from .views import BookmarkListCreateView, BookmarkDetailView, home

urlpatterns = [
    path('', home, name='home'),
    path('api/bookmarks/', BookmarkListCreateView.as_view()),
    path('api/bookmarks/<int:pk>/', BookmarkDetailView.as_view()),
]