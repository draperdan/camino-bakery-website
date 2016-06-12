from datetime import date

from django.db import models


class Schedule(models.Model):
    MONDAY_SCHEDULE = 0
    TUESDAY_SCHEDULE = 1
    WEDNESDAY_SCHEDULE = 2
    THURSDAY_SCHEDULE = 3
    FRIDAY_SCHEDULE = 4
    SATURDAY_SCHEDULE = 5
    SUNDAY_SCHEDULE = 6
    SCHEDULE_CHOICES = (
        (MONDAY_SCHEDULE, 'Monday'),
        (TUESDAY_SCHEDULE, 'Tuesday'),
        (WEDNESDAY_SCHEDULE, 'Wednesday'),
        (THURSDAY_SCHEDULE, 'Thursday'),
        (FRIDAY_SCHEDULE, 'Friday'),
        (SATURDAY_SCHEDULE, 'Saturday'),
        (SUNDAY_SCHEDULE, 'Sunday'),
    )
    day = models.IntegerField(choices=SCHEDULE_CHOICES)
    open_hour = models.TimeField()
    close_hour = models.TimeField()

    class Meta:
        ordering = ['day']

    @property
    def close_time_today(self):
        if date.today().weekday() == self.day:
            return True
