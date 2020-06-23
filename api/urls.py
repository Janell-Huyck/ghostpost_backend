from django.conf.urls import include, url

from api.views import GhostPostViewSet, BoastViewSet, RoastViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'roasts', RoastViewSet)
router.register(r'boasts', BoastViewSet)
router.register(r'ghostpost', GhostPostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
