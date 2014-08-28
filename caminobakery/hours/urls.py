from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from .views import HoursView

urlpatterns = patterns('',	
	url(r'^$', HoursView.as_view()),
)