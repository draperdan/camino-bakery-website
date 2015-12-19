from django.contrib.sitemaps import Sitemap
from news.models import Story


class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Story.live.all()

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, obj):
        return "/news/%s" % obj.slug
