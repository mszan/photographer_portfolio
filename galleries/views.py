from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from galleries.models import Gallery


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'galleries/gallery_detail.html'

    def get_context_data(self, **kwargs):
        gallery = get_object_or_404(Gallery, id=self.kwargs.get('pk'))
        images = gallery.images.all()
        return {'gallery': gallery, 'images': images}
