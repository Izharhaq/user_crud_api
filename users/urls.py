from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, find_users, save_users

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('find_users/', find_users),
    path('save_users/', save_users),
]
