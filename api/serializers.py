from rest_framework.serializers import HyperlinkedModelSerializer

from post.models import GhostPost


class GhostPostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GhostPost
        basename = 'posts'
        fields = (
            'id',
            'is_boast',
            'text',
            'up_votes',
            'down_votes',
            'submission_time',
            'score',
        )


class RoastSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GhostPost
        basename = 'roasts'
        fields = (
            'id',
            'is_boast',
            'text',
            'up_votes',
            'down_votes',
            'submission_time',
            'score',
        )


class BoastSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GhostPost
        basename = 'boasts'
        fields = (
            'id',
            'is_boast',
            'text',
            'up_votes',
            'down_votes',
            'submission_time',
            'score',
        )
