
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from tweet_app.models import TweetModel
from tweet_app.models import Comment
from tweet_app.models import RetweetModel
from tweet_app.serializers import TweetSerializer
from tweet_app.serializers import CommentSerializer
from tweet_app.serializers import RetweetSerializer
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from better_profanity import profanity

User = get_user_model()

@api_view(['GET'])
def get_comments_by_tweet_id(request, tweet_id):
    try:
        comments = Comment.objects.filter(tweet_id=tweet_id)
    except Comment.DoesNotExist:
        return Response({"error": "Comments not found for the provided tweet ID."},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

class TweetViewSet(viewsets.ModelViewSet):
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer
      
    def create(self, request, *args, **kwargs):
        # Extract user ID and tweet content from the request data
        author_id = request.data.get('author')
        content = request.data.get('content')
        
        is_profanity = profanity.contains_profanity(content)

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

        if is_profanity:
            print("error")
            return Response({
                "error": "Your Post contain Bad words, Please use appropriate language "              
                },)
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
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        # Extract user ID and comment content from the request data
        tweet_id = request.data.get('tweet_id')
        author_id = request.data.get('author_id')    
        content = request.data.get('content')
      


        if not content:
            return Response({"error": "Comment content is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the tweet with the provided ID exists
        try:
            tweet = TweetModel.objects.get(pk=tweet_id)
        except TweetModel.DoesNotExist:
            return Response({"error": "Tweet  does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user with the provided ID exists
        try:
            user = User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return Response({"error": "User  does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # Create the comment instance
        comment = Comment(tweet=tweet, author=user, content=content)
        comment.save()

        # Serialize the comment data and return it in the response
        serializer = CommentSerializer(comment)
        response_data = serializer.data
        response_data['author_name'] = user.username
        return Response(response_data, status=status.HTTP_201_CREATED, )
      

class RetweetViewSet(viewsets.ModelViewSet):
    queryset = RetweetModel.objects.all()
    serializer_class = RetweetSerializer

    @action(detail=True, methods=['post'])
    def create_retweet(self, request, pk=None):
        print("hii")
        # Extract the required data from the request
        author_id = request.data.get('author')
        tweet_id = request.data.get('tweet')
        content = request.data.get('retweet')

        try:
            user = User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return Response({"message": "User does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the retweet
        retweet = RetweetModel(author=user, tweet_id=tweet_id, retweet=content)
        retweet.save()

        serializer = RetweetSerializer(retweet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        # Get the author ID from the request query parameters
        author_id = self.request.query_params.get('author_id')

        if not author_id:
            # If author_id is not provided, return all tweets
            return RetweetModel.objects.all()

        # Check if the user with the provided ID exists
        try:
            user = User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return RetweetModel.objects.none()

        # Return the tweets authored by the user
        return RetweetModel.objects.filter(author=user)
    
    @action(detail=True, methods=['post'])
    def like_retweet(self, request, pk=None):
        retweet = self.get_object()  # Get the tweet instance
        user_id = request.data.get('user_id')  # Get the user ID from the request data

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"message": "User does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)

        if retweet.users_like.filter(pk=user.pk).exists():
            return Response({"message": "User has already liked this tweet."},
                            status=status.HTTP_400_BAD_REQUEST)

        retweet.users_like.add(user)
        serializer = RetweetSerializer(retweet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def unlike_retweet(self, request, pk=None):
        retweet = self.get_object()  # Get the tweet instance
        user_id = request.data.get('user_id')  # Get the user ID from the request data

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"message": "User does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)

        if not retweet.users_like.filter(pk=user.pk).exists():
            return Response({"message": "User has not liked this tweet."},
                            status=status.HTTP_400_BAD_REQUEST)

        retweet.users_like.remove(user)
        serializer = RetweetSerializer(retweet)
        return Response(serializer.data, status=status.HTTP_200_OK)