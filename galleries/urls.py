from django.shortcuts import redirect
from django.urls import path
from galleries.views import GallerySmallView, GalleryBigView
from .models import Gallery


urlpatterns = [
    # Landing url that redirect to first found gallery with index 0.
    path('',
         lambda request: redirect(f'galleries/{Gallery.objects.filter(main=True).first().id}/big/', permanent=False),
         name='galleries-landing'),

    # Big gallery url.
    path('galleries/<int:pk>/big/', GalleryBigView.as_view(), name='galleries-big'),

    # Small gallery url.
    path('galleries/<int:pk>/small/', GallerySmallView.as_view(), name='galleries-small'),
]
