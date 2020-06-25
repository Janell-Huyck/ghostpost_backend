from django.conf.urls import include, url
# from django.urls import path

from api.views import (GhostPostViewSet,
                       BoastViewSet,
                       RoastViewSet,)

#    GhostPostCreateView)

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'roasts', RoastViewSet, basename='roasts')
router.register(r'boasts', BoastViewSet, basename='boasts')
router.register(r'ghostpost', GhostPostViewSet, basename='posts')


urlpatterns = [
    # path('create/', GhostPostCreateView.as_view()),
    url(r'^api/', include(router.urls)),

]
