from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()
class TweetModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=280, verbose_name="tweet")
    photo = models.ImageField(upload_to='tweet_photos/', blank=True, null=True)
    users_like = models.ManyToManyField(User,
                                 related_name='tweets_liked',
                                 blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    # is_liked = models.BooleanField(default=False)
    

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.author.first_name} writes {self.body[:20]}...'

    @property
    def like_count(self):
        return self.users_like.all().count()


class CommentModel(models.Model):
    tweet = models.ForeignKey('TweetModel', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="comment")
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.author.username} on tweet by {self.tweet.author.username}'





    
    
    
class Mention(models.Model):
    author = models.ForeignKey(User,
                               related_name='mentions',
                               on_delete=models.CASCADE)
    tweet = models.ForeignKey(TweetModel,
                              related_name='mentions',
                              on_delete=models.CASCADE)
    mention = models.CharField(max_length=280, verbose_name="mention")
    users_like = models.ManyToManyField(User,
                                 related_name='mentions_liked',
                                 blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.author.username} mention to {self.tweet.body[:10]} with {self.mention[:10]}'

    
    def like_count(self):
        return self.users_like.all().count()

class Retweet(models.Model):
    author = models.ForeignKey(User,
                               related_name='retweet',
                               on_delete=models.CASCADE)
    tweet = models.ForeignKey(TweetModel,
                              related_name='retweet',
                              on_delete=models.CASCADE)
    retweet = models.CharField(max_length=280, verbose_name="retweet")
    users_like = models.ManyToManyField(User,
                                 related_name='retweet_liked',
                                 blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.author.username} retweet to {self.tweet.body[:10]} with {self.retweet[:10]}'

    
    def like_count(self):
        return self.users_like.all().count()
