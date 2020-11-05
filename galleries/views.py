from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from galleries.models import Gallery


class GalleryListView(ListView):
    model = Gallery
    template_name = 'galleries/gallery_list.html'
    context_object_name = 'galleries'
    ordering = ['index']

    def get_queryset(self, **kwargs):
        galleries = Gallery.objects.filter(visible=True)
        return galleries


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'galleries/gallery_detail.html'

    def get_context_data(self, **kwargs):
        gallery = get_object_or_404(Gallery, id=self.kwargs.get('pk'))
        images = gallery.images.all()
        return {'gallery': gallery, 'images': images}
