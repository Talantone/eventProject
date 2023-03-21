from django.contrib import admin
from scheduleEvents.models import Profile, ConferenceRoom, CalendarEvent

admin.site.register(Profile)
admin.site.register(ConferenceRoom)
admin.site.register(CalendarEvent)
