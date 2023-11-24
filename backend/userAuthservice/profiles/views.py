from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Profile, Contact
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, ContactSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    # The function is use to get profile data by user id
    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')  
        user = get_object_or_404(User, id=user_id) 
        profile = get_object_or_404(Profile, user=user)  
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    # Getting all followers and following users
    @action(detail=False, methods=['post'])
    # Custom action to follow a user
    def follow(self, request):
        user_from_id = request.data.get('user_from')
        user_to_id = request.data.get('user_to')
            
        user_from = Profile.objects.filter(user__id=user_from_id).first()
        user_to = Profile.objects.filter(user__id=user_to_id).first()
   
        if user_from is None or user_to is None:
            return Response({'message': 'Profiles for both users do not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        if not user_from.user.following.filter(id=user_to.user.id).exists():

            Contact.objects.create(user_from=user_from.user, user_to=user_to.user,is_followers=True)           
            return Response({'message': 'User followed successfully.'})
        return Response({'message': 'User is already followed.'})

    @action(detail=False, methods=['post'])
    def unfollow(self, request):
        user_from_id = request.data.get('user_from')
        user_to_id = request.data.get('user_to')

        user_from = get_object_or_404(User, id=user_from_id)
        user_to = get_object_or_404(User, id=user_to_id)
        print(user_from)
        print(user_to)
        try:
            contact = Contact.objects.get(user_from=user_from, user_to=user_to)
            contact.delete()
            return Response({'message': 'User unfollowed successfully.'})
        except Contact.DoesNotExist:
            return Response({'message': 'User is not followed yet.'})


