from django.urls import path
from .views import EventAPIList

app_name = 'scheduleEvents'

urlpatterns = [
    path(r'events/', EventAPIList.as_view(), name='events'),
]
