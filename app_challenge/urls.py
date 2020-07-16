from django.urls import path, include
from . import views
from rest_framework import routers

# set URLs for the app "app_challenge"

router = routers.DefaultRouter()  # https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router.register('occurrence', views.OccurrenceView)
router.register('category', views.CategoryView)

urlpatterns = [
    path('', include(router.urls)),
]
