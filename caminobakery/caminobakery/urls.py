from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.sitemaps import FlatPageSitemap

from django.contrib import admin
admin.autodiscover()

from .views import HomePageView, RobotsView
from news.feeds import LatestStories, LatestStoriesByCategory
from sitemaps import NewsSitemap

sitemaps = {
    'news': NewsSitemap,
    'flatpages': FlatPageSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^feeds/news/$', LatestStories()),
    url(r'^feeds/categories/(?P<slug>[-\w]+)/$', LatestStoriesByCategory()),
    url(r'^hours-location/', include('hours.urls')),
    url(r'^specials/', include('specials.urls')),
    url(r'^menu/', include('menu.urls')),
    url(r'^news/', include('news.urls')),

    # Not ready for prime-time
    #url(r'^order/', include('order_form.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+).xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^$', HomePageView.as_view()),
    url(r'^robots\.txt$', RobotsView.as_view()),

)

urlpatterns += patterns('django.contrib.flatpages.views', url(r'^(?P<url>.*/)$', 'flatpage'),)

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
