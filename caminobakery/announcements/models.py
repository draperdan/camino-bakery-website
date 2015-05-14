from django.db import models


class PublicAnnouncementManager(models.Manager):
    """
    Manager which will only fetch public Announcements.
    """
    def get_queryset(self):
        return super(
            PublicAnnouncementManager, self).get_queryset().filter(
                is_public=True)


class Announcement(models.Model):
    """
    A simple, site-wide announcement bar.
    """
    text = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters. Plain text only.',
        default='',
    )
    link = models.URLField(
        blank=True,
        help_text='Optional. Used to link the entire announcement.',
        default='',
    )
    is_public = models.BooleanField(
        default=False,
        help_text='Determines if announcement is displayed on the website.',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text='Timestamp when this announcement was created.',
    )
    objects = models.Manager()
    public = PublicAnnouncementManager()

    def __unicode__(self):
        return self.text

    def save(self, *args, **kwargs):
        """
        On save, check if is_public is True. If so, set this value for other
        announcements to False.
        """
        if self.is_public:
            Announcement.objects.exclude(pk=self.pk).update(is_public=False)
        super(Announcement, self).save(*args, **kwargs)
