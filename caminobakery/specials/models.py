from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from datetime import date

from django.db import models


class SpecialTodayManager(models.Manager):
    def get_queryset(self):
        return super(SpecialTodayManager, self).get_queryset().filter(
            day_offered=date.today().weekday())


@python_2_unicode_compatible
class Special(models.Model):
    MONDAY_SPECIAL = 0
    TUESDAY_SPECIAL = 1
    WEDNESDAY_SPECIAL = 2
    THURSDAY_SPECIAL = 3
    FRIDAY_SPECIAL = 4
    SATURDAY_SPECIAL = 5
    SUNDAY_SPECIAL = 6
    SPECIAL_CHOICES = (
        (MONDAY_SPECIAL, 'Monday'),
        (TUESDAY_SPECIAL, 'Tuesday'),
        (WEDNESDAY_SPECIAL, 'Wednesday'),
        (THURSDAY_SPECIAL, 'Thursday'),
        (FRIDAY_SPECIAL, 'Friday'),
        (SATURDAY_SPECIAL, 'Saturday'),
        (SUNDAY_SPECIAL, 'Sunday'),
    )
    description = models.CharField(
        max_length=250, help_text='Limited to 250 characters.')
    day_offered = models.IntegerField(choices=SPECIAL_CHOICES)
    objects = models.Manager()
    today = SpecialTodayManager()

    class Meta:
        verbose_name_plural = 'Specials'
        ordering = ['day_offered']

    def __str__(self):
        return "{} on {}".format(self.description, self.day_offered)

    @property
    def special_today(self):
        if date.today().weekday() == self.day_offered:
            return True
