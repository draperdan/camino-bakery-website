from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.flatpages import views

from django.contrib import admin
admin.autodiscover()

from .views import HomePageView, RobotsView

sitemaps = {
    'flatpages': FlatPageSitemap,
}

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hours-location/', include('hours.urls')),
    url(r'^specials/', include('specials.urls')),
    url(r'^menu/', include('menu.urls')),
    # NOTE: We're redirecting all news stories to the homepage since this
    # app isn't used currently.
    url(r'^news/', RedirectView.as_view(
        permanent=False, url='http://caminobakery.com')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+).xml$',
        'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^$', HomePageView.as_view()),
    url(r'^robots\.txt$', RobotsView.as_view()),
]

urlpatterns += [
    url(r'^(?P<url>.*/)$', views.flatpage),
]

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
