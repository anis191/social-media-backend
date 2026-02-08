from django.urls import path,include
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from users.views import *
from posts.views import *

router = routers.DefaultRouter()
router.register('profiles', UserProfileViewSet, basename='profile')
router.register('posts', PostViewSet, basename='post')

post_router = routers.NestedDefaultRouter(router, 'posts', lookup = 'posts')
post_router.register('media', PostMediaViewSet, basename='post_media')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(post_router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]