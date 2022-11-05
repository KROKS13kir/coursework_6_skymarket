from django.conf import settings
from django.db import models

from ads.models.ad import Ad


class Comment(models.Model):
    text = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.title