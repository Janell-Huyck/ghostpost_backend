from django.db import models
# from django.utils import timezone
# from datetime import datetime


class GhostPost(models.Model):
    is_boast = models.BooleanField()
    text = models.CharField(max_length=280)
    up_votes = models.IntegerField(
        default=0, editable=False, null=True, blank=True)
    down_votes = models.IntegerField(
        default=0, editable=False, null=True, blank=True)
    submission_time = models.DateTimeField(
        auto_now_add=True, editable=False, null=False, blank=False)
    score = models.IntegerField(
        editable=False, default=0, null=True, blank=True)

    def save(self, *args, **kwargs):

        self.score = self.up_votes - self.down_votes
        super(GhostPost, self).save()

    def score(self):
        score = self.up_votes - self.down_votes
        return score
