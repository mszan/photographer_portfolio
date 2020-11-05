from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from .views import AboutView


urlpatterns = [
    path('about/',
         AboutView.as_view(),
         name='infos-about'),
]