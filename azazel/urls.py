from django.conf.urls import url, include
from rest_framework import routers
from azazel.api import views

router = routers.DefaultRouter()
router.register(r"events", views.EventViewSet)
router.register(r"courses", views.CourseViewSet)
router.register(r"users", views.UserViewSet)
router.register(r"talks", views.TalkViewSet)
router.register(r"workshops", views.WorkshopViewSet)
router.register(r"keynotes", views.KeynoteViewSet)
router.register(r"user_talk", views.UserTalkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
