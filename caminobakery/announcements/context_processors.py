from django.core.exceptions import ObjectDoesNotExist

from .models import Announcement


def current_announcement(request):
    """
    Context processor for the current announcement.
    """
    try:
        announcement = Announcement.public.latest('created')
    except ObjectDoesNotExist:
        announcement = None
    return {
        'announcement': announcement
    }
