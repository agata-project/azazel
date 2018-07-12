from .models import Course, Event, User, Talk, Workshop, Keynote, UserTalk
from rest_framework import viewsets
from azazel.api.serializers import EventSerializer, CourseSerializer, UserSerializer, TalkSerializer, WorkshopSerializer, KeynoteSerializer, UserTalkSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TalkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer


class WorkshopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class KeynoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Keynote.objects.all()
    serializer_class = KeynoteSerializer


class UserTalkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserTalk.objects.all()
    serializer_class = UserTalkSerializer
