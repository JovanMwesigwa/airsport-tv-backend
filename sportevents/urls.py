
# import path
from django.urls import path

from .views import (
    SportEventListView,
    GetMainEventView,
    GetLiveSportEventsListView,
    GetFinishedSportEventsListView,
    GetUpcomingSportEventsListView,
    GetFilteredSportEventsListView,
    GetEventDetails,
    get_event_link,
    GetEventMedia
)

urlpatterns = [
    path('', SportEventListView.as_view(), name='sportevents-list'),
    path('main/', GetMainEventView.as_view(), name='main-sport-event'),
    path('live/', GetLiveSportEventsListView.as_view(), name='live-sport-event'),
    path('upcoming/', GetUpcomingSportEventsListView.as_view(),
         name='upcoming-sport-event'),
    path('finished/', GetFinishedSportEventsListView.as_view(),
         name='finished-sport-event'),
    path('<pk>/detail', GetEventDetails.as_view(), name="event-details"),
    path('<category_id>/', GetFilteredSportEventsListView.as_view(),
         name='finished-sport-event'),
    path('<pk>/link', GetEventMedia.as_view(), name="event-link")
]
