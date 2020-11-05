from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from galleries.views import GalleryListView, GalleryDetailView

urlpatterns = [
    path('',
         GalleryListView.as_view(),
         name='galleries-list'),

    path('galleries/<int:pk>',
         GalleryDetailView.as_view(),
         name='galleries-detail'),
]
