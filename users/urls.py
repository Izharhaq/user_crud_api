from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserList, UserCreate, UserUpdate, UserDelete, UserFind, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserList.as_view(), name='list_users'),
    path('users/add/', UserCreate.as_view(), name='add_user'),
    path('users/update/<int:pk>/', UserUpdate.as_view(), name='update_user'),
    path('users/delete/<int:pk>/', UserDelete.as_view(), name='delete_user'),
    path('users/find/', UserFind.as_view(), name='find_users'),
]
