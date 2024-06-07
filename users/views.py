from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def find_users(request):
    users = User.objects.filter(
        firstName=request.data['firstName'], 
        lastName=request.data['lastName'], 
        phone=request.data['phone'], 
        dateOfBirth=request.data['dateOfBirth']
    )
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_users(request):
    try:
        user = User.objects.get(id=request.data['userId'])
    except User.DoesNotExist:
        user = User()

    user.firstName = request.data['firstName']
    user.lastName = request.data['lastName']
    user.middleName = request.data['middleName']
    user.dateOfBirth = request.data['dateOfBirth']
    user.email = request.data['email']
    user.phone = request.data['phone']
    user.save()

    return Response(status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Check
