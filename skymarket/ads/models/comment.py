from django.db import models

from ads.models.ad import Ad
from users.models import User


class Comment(models.Model):
    text = models.TextField(blank=True, max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.title