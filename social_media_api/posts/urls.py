from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from .views import FeedViewSet

feed_list = FeedViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('feed/', feed_list, name='feed'),
]
