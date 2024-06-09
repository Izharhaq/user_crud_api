from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdate(APIView):
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDelete(APIView):
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserFind(APIView):
    def get(self, request):
        first_name = request.query_params.get('firstName', None)
        last_name = request.query_params.get('lastName', None)
        phone = request.query_params.get('phone', None)
        date_of_birth = request.query_params.get('dateOfBirth', None)

        filters = {}
        if first_name:
            filters['first_name'] = first_name
        if last_name:
            filters['last_name'] = last_name
        if phone:
            filters['phone'] = phone
        if date_of_birth:
            filters['date_of_birth'] = date_of_birth

        users = User.objects.filter(**filters)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
