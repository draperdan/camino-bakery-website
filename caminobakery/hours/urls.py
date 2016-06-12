from django.conf.urls import url

from .views import HoursView

urlpatterns = [
    url(r'^$', HoursView.as_view()),
]
