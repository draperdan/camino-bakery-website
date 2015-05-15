from django.views.generic import DateDetailView, ListView
from news.models import Story


class StoryDetailView(DateDetailView):

    date_field = "pub_date"
    template_name = "news/story_detail.html"
    context_object_name = "story"
    slug_field = "slug"

    def get_queryset(self):
        stories = None
        if self.request.user.is_staff:
            stories = Story.objects.all()
        else:
            stories = Story.live.all()
        return stories


class StoryListView(ListView):
    """ View to display all stories. Includes context to get the
    latest story for special treatment in template.
    """

    allow_empty = True
    context_object_name = "story_list"
    queryset = Story.live.all().order_by('-pub_date')
    template_name = "news/story_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        context['latest_story'] = Story.live.latest('pub_date')
        return context
