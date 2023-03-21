import datetime

import pytz
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from scheduleEvents.models import CalendarEvent, Profile
from scheduleEvents.serializers import EventSerializer
from scheduleEvents.permissions import IsOwnerOrManager
from scheduleEvents.logic import time_to_tz_naive


class EventAPIList(generics.ListCreateAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrManager,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location_id", "start", "event_name", "agenda"]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset.filter(Q(owner=self.request.user) | Q(location__manager=self.request.user) | Q(participant_list=self.request.user)).distinct()
        profile = Profile.objects.get(user=self.request.user)
        tz = profile.timezone
        qs_to_update = list(queryset)
        for i in range(len(qs_to_update)):
            qs_to_update[i].start = str(time_to_tz_naive(qs_to_update[i].start, pytz.utc, pytz.timezone(tz)))
            qs_to_update[i].end = str(time_to_tz_naive(qs_to_update[i].end, pytz.utc, pytz.timezone(tz)))

        queryset.bulk_update(qs_to_update, ["start", "end"])
        return queryset
