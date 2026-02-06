from django.urls import path,include
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from users.views import *

router = routers.DefaultRouter()
router.register('profiles', UserProfileViewSet, basename='profile')

urlpatterns = [
    path('',include(router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]