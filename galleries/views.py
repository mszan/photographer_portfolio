from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from galleries.models import Gallery


class GallerySmallView(DetailView):
    model = Gallery
    template_name = 'galleries/gallery_small.html'

    def get_context_data(self, **kwargs):
        gallery = get_object_or_404(Gallery, id=self.kwargs.get('pk'))
        images = gallery.images.filter(visible=1).order_by('index')
        return {'gallery': gallery,
                'images': images,
                'page_title': gallery.title,
                'list_for_random_margin': range(2, 10)}


class GalleryBigView(DetailView):
    model = Gallery
    template_name = 'galleries/gallery_big.html'

    def get_context_data(self, **kwargs):
        gallery = get_object_or_404(Gallery, id=self.kwargs.get('pk'))
        images = gallery.images.filter(visible=1).order_by('index')
        return {'gallery': gallery,
                'images': images,
                'page_title': gallery.title}
