from django.contrib import admin
from django.urls import path, include
from tweet_app.views import TweetViewSet
from tweet_app.views import CommentViewSet,RetweetViewSet
from rest_framework import routers

from .views import get_comments_by_tweet_id

router = routers.DefaultRouter()
router.register(r'tweet', TweetViewSet, basename="tweet")
router.register(r'comment', CommentViewSet, basename="comment")
router.register(r'retweet', RetweetViewSet, basename="retweet")

urlpatterns = [ 
    path("", include(router.urls)),
    path('comments/tweet/<int:tweet_id>/', get_comments_by_tweet_id, name='get_comments_by_tweet_id'),
    path('retweet/<int:pk>/like/', RetweetViewSet.as_view({'post': 'like_retweet'}), name='like-retweet'),
    path('retweet/<int:pk>/unlike/', RetweetViewSet.as_view({'post': 'unlike_retweet'}), name='unlike-retweet'),

]
