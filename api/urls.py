from django.urls import path,include
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from users.views import UserViewSet

router = routers.DefaultRouter()
# router.register('users', UserViewSet)

urlpatterns = [
    path('',include(router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]