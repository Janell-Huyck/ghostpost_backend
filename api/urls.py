from django.conf.urls import include, url
from rest_framework import routers


from api.views import (GhostPostViewSet,
                       BoastViewSet,
                       RoastViewSet,)


router = routers.DefaultRouter()

router.register(r'roasts', RoastViewSet, basename='roasts')
router.register(r'boasts', BoastViewSet, basename='boasts')
router.register(r'ghostpost', GhostPostViewSet, basename='posts')


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
