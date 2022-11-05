from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=0)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ads_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'

    def __str__(self):
        return self.title