

from rest_framework import serializers
from .models import TweetModel
from django.contrib.auth import get_user_model
User = get_user_model()

class TweetSerializer(serializers.ModelSerializer):
    # Using PrimaryKeyRelatedField to represent the user foreign key relationship
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = TweetModel
        # Include 'author' field in the 'fields' option
        fields = ('id', 'author', 'body', 'created', 'updated', 'users_like', )