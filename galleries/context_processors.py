from .models import Gallery


def get_all_galleries(request):
    """
    Function that returns active galleries objects.
    """
    return {'cp_galleries': Gallery.objects.filter(visible=1).order_by('index')}
