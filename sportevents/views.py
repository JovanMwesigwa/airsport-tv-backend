from django.shortcuts import render

from .models import SportEvent, Category
from .serializers import SportEventSerializer, SportEventMediaSerializer, CategorySerializer, SportEventReadOnlySerializer, CategoryReadOnlySerializer, SportEventDataOnlySerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def get_event_link(request, pk):
    try:
        #    get the Evevnt mopdel
        event = SportEvent.objects.get(id=pk)
        event_media = event.event_media
        serializer = SportEventMediaSerializer(event)
        if serializer:
            return Response({
                "response": serializer.data
            })
        else:
            return Response({"response": "We could not find the link"})
    except:
        return Response({"response": "We could not find the link"})


class SportEventListView(ListAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventReadOnlySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return SportEvent.objects.filter(isSport=True)


class GetMainEventView(RetrieveAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventReadOnlySerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return SportEvent.objects.filter(main=True).first()


class GetLiveSportEventsListView(ListAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventDataOnlySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        first_six = SportEvent.objects.filter(
            status='live').order_by('start_date')[:6]
        return first_six


class GetUpcomingSportEventsListView(ListAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventDataOnlySerializer
    permission_classes = (AllowAny,)

    # filter only the upcoming events
    def get_queryset(self):
        return SportEvent.objects.filter(status="upcoming").order_by('start_date')[:6]


class GetFinishedSportEventsListView(ListAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventDataOnlySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return SportEvent.objects.filter(status="finished").order_by('start_date')[:6]


class GetFilteredSportEventsListView(ListAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventDataOnlySerializer
    permission_classes = (AllowAny,)
    # kwargs = {'category_id': category_id}

    def get_queryset(self, *args, **kwargs):
        category_id = self.kwargs['category_id']
        if category_id is not None:
            return SportEvent.objects.filter(category_id=category_id)


class GetEventDetails(RetrieveAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventDataOnlySerializer
    permission_classes = (AllowAny,)


class GetEventMedia(RetrieveAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventMediaSerializer
    permission_classes = (AllowAny,)
