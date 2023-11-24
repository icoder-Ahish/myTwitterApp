

from rest_framework import serializers
from .models import TweetModel
from .models import Comment
from .models import RetweetModel
from django.contrib.auth import get_user_model
User = get_user_model()

class TweetSerializer(serializers.ModelSerializer):
    # Using PrimaryKeyRelatedField to represent the user foreign key relationship
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = TweetModel
        # Include 'author' field in the 'fields' option
        fields = ('id', 'author', 'body', 'created', 'updated', 'users_like', )
        


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author_name(self, obj):
        return obj.author.username       
    
class RetweetSerializer(serializers.ModelSerializer):    
    # tweet = TweetSerializer()
    class Meta:
        model = RetweetModel
        fields = '__all__'