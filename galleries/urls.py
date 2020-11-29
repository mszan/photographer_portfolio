from django.shortcuts import redirect
from django.urls import path
from galleries.views import GallerySmallView, GalleryBigView, GalleryLandingView
from .models import Gallery


urlpatterns = [
    # Landing url.
    path('', GalleryLandingView.as_view(), name='landing'),

    # Big gallery url.
    path('galleries/<int:pk>/big/', GalleryBigView.as_view(), name='galleries-big'),

    # Small gallery url.
    path('galleries/<int:pk>/small/', GallerySmallView.as_view(), name='galleries-small'),
]
