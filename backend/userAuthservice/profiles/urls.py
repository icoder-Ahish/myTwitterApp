from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ProfileViewSet, ContactViewSet

# Create a router and register the viewsets with it.
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename="profiles")
router.register(r'contacts', ContactViewSet, basename="Contacts")

urlpatterns = [
    path('', include(router.urls)),
   path('notification/', ContactViewSet.as_view({'get': 'get_follow_message'}), name='contact-follow-message')
]

# Include the router URLs


