from .models import Announcement


def current_announcement(request):
    """
    Context processor for the current announcement.
    """
    return {'announcement': Announcement.public.latest('created')}
