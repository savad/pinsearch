from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from pin_search.api import PinSearchAPIView

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^search/$', PinSearchAPIView.as_view(), name='search'),
]