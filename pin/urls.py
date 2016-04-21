from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from pin_search.api import PinSearchViewSet

router = routers.DefaultRouter()
router.register(r'search', PinSearchViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]