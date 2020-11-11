from infos.models import Social


def get_all_socials(request):
    """
    Function that returns active galleries objects.
    """
    return {'cp_socials': Social.objects.filter(visible=True).order_by('index')}
