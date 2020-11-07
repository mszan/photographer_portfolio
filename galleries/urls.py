from django.shortcuts import redirect
from django.urls import path
from galleries.views import GalleryDetailView
from .models import Gallery


urlpatterns = [
    # Landing url that redirect to first found gallery with index 0.
    path('',
         lambda request: redirect(f'galleries/{Gallery.objects.filter(index=0).first().id}',permanent=False),
         name='galleries-landing'),

    # Gallery details url.
    path('galleries/<int:pk>/',
         GalleryDetailView.as_view(),
         name='galleries-detail'),
]
