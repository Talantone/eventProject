

from rest_framework import serializers
from django.utils import timezone

from rest_framework.exceptions import ValidationError

from scheduleEvents.models import CalendarEvent


class DateTimeTzAwareField(serializers.DateTimeField):

    def to_native(self, value):
        value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_representation(value)


class EventSerializer(serializers.ModelSerializer):
    start = DateTimeTzAwareField()
    end = DateTimeTzAwareField()

    class Meta:
        model = CalendarEvent
        fields = ("owner", "event_name", "agenda", "start", "end", "participant_list", "location")

    def validate(self, attrs):
        start = attrs.get("start")
        end = attrs.get("end")
        if start and end:
            delta = end - start
            if delta.total_seconds() > 3600:
                msg = ("Can't create event longer than 8 hours")
                raise ValidationError(msg)
            return attrs
