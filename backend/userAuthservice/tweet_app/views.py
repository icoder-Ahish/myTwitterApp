
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import TweetModel
from .serializers import TweetSerializer
from rest_framework.decorators import action

User = get_user_model()

class TweetViewSet(viewsets.ModelViewSet):
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer

      

    def create(self, request, *args, **kwargs):
        # Extract user ID and tweet content from the request data
        author_id = request.data.get('author')
        content = request.data.get('content')

        if not author_id:
            return Response({"error": "User ID is required."},
                            status=status.HTTP_400_BAD_REQUEST)

        if not content:
            return Response({"error": "Tweet content is required."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the user with the provided ID exists
        try:
            user = User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return Response({"error": "User with the provided ID does not exist."},
                            status=status.HTTP_404_NOT_FOUND)

        # Create the tweet instance
        tweet = TweetModel(author=user, body=content)
        tweet.save()

        # Serialize the tweet data and return it in the response
        serializer = TweetSerializer(tweet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        # Get the author ID from the request query parameters
        author_id = self.request.query_params.get('author_id')

        if not author_id:
            # If author_id is not provided, return all tweets
            return TweetModel.objects.all()

        # Check if the user with the provided ID exists
        try:
            user = User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return TweetModel.objects.none()

        # Return the tweets authored by the user
        return TweetModel.objects.filter(author=user)
    
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        tweet = self.get_object()  # Get the tweet instance
        user_id = request.data.get('user_id')  # Get the user ID from the request data

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"message": "User does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)

        if tweet.users_like.filter(pk=user.pk).exists():
            return Response({"message": "User has already liked this tweet."},
                            status=status.HTTP_400_BAD_REQUEST)

        tweet.users_like.add(user)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        tweet = self.get_object()  # Get the tweet instance
        user_id = request.data.get('user_id')  # Get the user ID from the request data

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"message": "User does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)

        if not tweet.users_like.filter(pk=user.pk).exists():
            return Response({"message": "User has not liked this tweet."},
                            status=status.HTTP_400_BAD_REQUEST)

        tweet.users_like.remove(user)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data, status=status.HTTP_200_OK)