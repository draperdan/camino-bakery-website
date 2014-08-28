from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import utc

from categories.models import Category
from media.models import Photo

import datetime
from markdown import markdown
from typogrify.filters import typogrify


def markup(text):
    """
    Mark up plain text into fancy HTML.
    """
    return typogrify(markdown(text, lazy_ol=False, output_format='html5', extensions=['abbr', 'codehilite', 'fenced_code', 'sane_lists', 'smart_strong']))


class LiveStoryManager(models.Manager):
    """
    Manager which will only fetch live entries.
    """
    def get_query_set(self):
        return super(LiveStoryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)


class Story(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
    )
    headline = models.CharField(max_length='250', help_text='Limited to 250 characters.')
    slug = models.SlugField(unique_for_date='pub_date', help_text='Suggested value automatically generated from name. Must be unique for a given pub date.')
    pub_date = models.DateTimeField(default=datetime.datetime.utcnow)
    body = models.TextField(help_text='A brief description of the item. No HTML is allowed; please use Markdown syntax.')
    body_html = models.TextField(editable=False, blank=True)
    excerpt = models.TextField(blank=True, null=True, help_text='A brief paragraph or so to entice readers to click to the full story. Used on the news indexes. No HTML is allowed.')
    lead_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='story_lead_photo', limit_choices_to={'status__in': [1]})
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    categories = models.ManyToManyField(Category, limit_choices_to={'itemtype__category_ptr__isnull': True, 'itemtypegroup__category_ptr__isnull': True})

    objects = models.Manager()
    live = LiveStoryManager()

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ('-pub_date',)
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return '/news/%s/%s/' % (self.pub_date.strftime('%Y/%b/%d').lower(), self.slug)

    @property
    def related_story_set(self):
        category_id_list = self.categories.values_list("id", flat=True)
        return Story.live.filter(categories__id__in=category_id_list).exclude(id=self.id).distinct()[:5]    

    def save(self, force_insert=False, force_update=False):
        self.body_html = markup(self.body)
        super(Story, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass
