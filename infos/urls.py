from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from .views import BioView


urlpatterns = [
    path('bio/',
         BioView.as_view(),
         name='infos-bio'),
]