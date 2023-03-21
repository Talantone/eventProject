from django.db import models
from django.contrib.auth.models import User
import pytz

from scheduleEvents.logic import convert_tz


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_id = models.IntegerField()

    TIMEZONES = convert_tz()

    timezone = models.CharField(max_length=255, choices=TIMEZONES, default='UTC')

    def __str__(self):
        return self.user.username


class ConferenceRoom(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class CalendarEvent(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    agenda = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    participant_list = models.ManyToManyField(User, related_name="participants")
    location = models.ForeignKey(ConferenceRoom, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name
