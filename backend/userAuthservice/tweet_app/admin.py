from django.contrib import admin
from tweet_app.models import TweetModel
from tweet_app.models import Comment
from tweet_app.models import RetweetModel
# Register your models here.


# Register your models here.

admin.site.register(TweetModel)
admin.site.register(Comment)
admin.site.register(RetweetModel)
