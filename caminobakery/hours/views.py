from django.views.generic import ListView

from .models import Schedule


class HoursView(ListView):
    """ View to display the operating schedule and hours. """

    context_object_name = "schedule_list"
    queryset = Schedule.objects.all()
    template_name = "hours/schedule_list.html"
