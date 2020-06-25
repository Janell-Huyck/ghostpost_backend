from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from api.serializers import (GhostPostSerializer,
                             BoastSerializer,
                             RoastSerializer)

from post.models import GhostPost


class GhostPostViewSet(ModelViewSet):
    basename = 'posts'
    serializer_class = GhostPostSerializer
    queryset = GhostPost.objects.all()

    @action(detail=True, methods=['post'])
    def likePost(self, request, pk=None):
        ghostpost = self.get_object()
        ghostpost.up_votes += 1
        ghostpost.save()
        return Response({'status': 'upvoted'})

    @action(detail=True, methods=['post'])
    def dislikePost(self, request, pk=None):
        ghostpost = self.get_object()
        ghostpost.down_votes += 1
        ghostpost.save()
        return Response({'status': 'downvoted'})


# class GhostPostCreateView(CreateAPIView):
#     basename = 'create_post'
#     serializer_class = GhostPostSerializer
#     queryset = GhostPost.objects.all()

    # def create(self, request):
    #     if request.method == "post":
    #         new_post = GhostPost.objects.create({
    #             "is_boast": request.is_boast,
    #             "text": request.text,
    #         })
    #         new_post.save()

    #         return Response({'status': 'post created'})


class BoastViewSet(ModelViewSet):
    basename = 'boasts'
    serializer_class = BoastSerializer
    queryset = GhostPost.objects.filter(is_boast=True)


class RoastViewSet(ModelViewSet):
    basename = 'roasts'
    serializer_class = RoastSerializer
    queryset = GhostPost.objects.filter(is_boast=False)
