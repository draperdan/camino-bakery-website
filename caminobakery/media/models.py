from __future__ import unicode_literals
import datetime

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User


class LivePhotoManager(models.Manager):
    def get_queryset(self):
        return super(LivePhotoManager, self).get_queryset().filter(
            status=self.model.LIVE_STATUS).filter(is_aggregated=True)


@python_2_unicode_compatible
class Photo(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
    )
    title = models.CharField(
        max_length=250,
        help_text='Limited to 250 characters. Will also be used for alt text.')
    slug = models.SlugField(
        help_text='This field will automatically populate from the title.',
        unique_for_date='uploaded')
    photo = models.ImageField(
        upload_to='images/photos',
        width_field='width',
        height_field='height',
        help_text='Please use JPG or PNG formats. Will populate the width '
                  'and height fields on save.')
    uploaded = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(auto_now=True)
    caption = models.TextField(
        help_text='A brief description of the photo. No HTML is allowed.',
        blank=True)
    photographer = models.ForeignKey(User, blank=True, null=True)
    one_off_photographer = models.CharField(max_length=100, blank=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    alt_text = models.CharField(
        max_length=200,
        help_text='Limited to 100 characters. Used for displaying text in '
                  'case image isn\'t viewable.')
    external_url = models.URLField(
        help_text='If the photo is located on an external website, '
                  'please add the URL here.', blank=True)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=2,
        help_text="Only photos with a status of 'live' will be displayed "
                  "publicly.")

    objects = models.Manager()
    live = LivePhotoManager()

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
        ordering = ['-uploaded']

    def __str__(self):
        return '%s' % self.title

    @property
    def get_photo_orientation(self):
        if self.height > self.width:
            return 'vertical'
        else:
            return 'horizontal'
