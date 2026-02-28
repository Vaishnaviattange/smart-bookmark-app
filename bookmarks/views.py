from rest_framework import generics
from .models import Bookmark
from .serializers import BookmarkSerializer
from django.shortcuts import render

# API Views
class BookmarkListCreateView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

# Frontend View
def home(request):
    return render(request, 'index.html')