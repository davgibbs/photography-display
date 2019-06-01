from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(r'photos', views.PhotoViewSet)
urlpatterns = router.urls
