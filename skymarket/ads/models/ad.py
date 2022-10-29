from django.db import models

from skymarket import settings


class Ad(models.Model):
    title = models.CharField(blank=False, max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='ads_images/', null=True)

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'

    def __str__(self):
        return self.title