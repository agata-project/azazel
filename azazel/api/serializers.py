from .models import Course, Event, User, Talk, Workshop, Keynote, UserTalk
from rest_framework import serializers


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'initials']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'course']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'course', 'email', 'cpf', 'registration']


class TalkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Talk
        fields = ['event', 'name', 'speaker',
                  'description', 'local', 'init_time', 'finish_time', 'date']


class WorkshopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workshop
        fields = ['event', 'name', 'speaker',
                  'description', 'local', 'init_time', 'finish_time', 'date', 'donate']


class KeynoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keynote
        fields = ['event', 'name', 'speaker',
                  'description', 'local', 'init_time', 'finish_time', 'date']


class UserTalkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTalk
        fields = ['talk', 'user']
