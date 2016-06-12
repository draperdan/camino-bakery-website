from django.conf.urls import url
from django.views.generic import (YearArchiveView, MonthArchiveView,
                                  DayArchiveView)
from django.views.decorators.cache import cache_page

from news.models import Story
from news.views import StoryDetailView, StoryListView

urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\w-]+)/$',
        StoryDetailView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',
        cache_page(60 * 15)(
            DayArchiveView.as_view(
                queryset=Story.live.all(),
                date_field="pub_date",
                template_name="news/story_archive_day.html",
                context_object_name="story_list",))),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
        cache_page(60 * 15)(
            MonthArchiveView.as_view(
                queryset=Story.live.all(),
                date_field="pub_date",
                template_name="news/story_archive_month.html",
                context_object_name="story_list",))),
    url(r'^(?P<year>\d{4})/$', cache_page(60 * 15)(YearArchiveView.as_view(
        queryset=Story.live.all(),
        date_field="pub_date",
        template_name="news/story_archive_year.html",
        context_object_name="story_list",
        make_object_list=True,
    ))),
    url(r'^$', cache_page(60 * 15)(StoryListView.as_view())),
]
