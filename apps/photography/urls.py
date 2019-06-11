from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from display.urls import router
from display import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
