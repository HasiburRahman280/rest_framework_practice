from django.contrib import admin
from django.urls import path, include
from api import views
# from .serializers import SongSerializer,SingerSerializer
from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter()

# register Student viewsset router
router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewSet, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]
