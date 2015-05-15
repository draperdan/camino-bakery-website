from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from .views import CakesView, ItemListView, CateringView
from .views import BreadView, SandwichView, AlcoholView

urlpatterns = patterns(
    '',
    url(r'^$', cache_page(60 * 15)(ItemListView.as_view())),
    url(r'^sandwiches/$', cache_page(60 * 15)(SandwichView.as_view())),
    url(r'^cakes/$', cache_page(60 * 15)(CakesView.as_view())),
    url(r'^catering/$', cache_page(60 * 15)(CateringView.as_view())),
    url(r'^bread/$', cache_page(60 * 15)(BreadView.as_view())),
    url(r'^wine-beer/$', cache_page(60 * 15)(AlcoholView.as_view())),
)
