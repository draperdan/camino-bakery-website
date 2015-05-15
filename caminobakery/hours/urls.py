from django.conf.urls import patterns, url

from .views import HoursView

urlpatterns = patterns(
    '',
    url(r'^$', HoursView.as_view()),
)
