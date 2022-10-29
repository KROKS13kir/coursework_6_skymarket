from django.urls import path, include

from ads.views.ad import AdViewSet
from ads.views.comment import CommentViewSet
from rest_framework import routers

ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet)
ads_router.register('ads/(?P<ad_id>[^/.]+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(ads_router.urls)),
]