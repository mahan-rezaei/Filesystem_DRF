from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

User = get_user_model()


class UserCreateView(APIView):
    """created a user with this view"""

    def post(self, request):
        ser_data = UserCreateSerializer(data=request.data)
        if ser_data.is_valid(raise_exception=True):
            user = ser_data.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_data': ser_data.data
            }, status=status.HTTP_201_CREATED)


class UserListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeActiveView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        user.is_active = False
        user.save()
        return Response({'message': 'user deactivated successfully.'}, status=status.HTTP_200_OK)



