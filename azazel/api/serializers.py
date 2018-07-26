from .models import Course, Event, User, Talk, Workshop, Keynote, UserTalk
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = "__all__"


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = "__all__"


class KeynoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keynote
        fields = "__all__"


class UserTalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTalk
        fields = "__all__"
