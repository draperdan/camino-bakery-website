from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from .models import Special

urlpatterns = patterns('',
	(r'^$', ListView.as_view(
		queryset = Special.objects.all(),
		context_object_name = "specials_list",
		template_name = "specials/specials_list.html",
	)),
)