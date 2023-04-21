from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    

class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    

class UserDestroy(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    #permission_classes = (IsAuthenticated, )
    

class RestaurantUpdate(generics.RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated, )


class RestaurantDestroy(generics.RetrieveDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated, )


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuVoteView(generics.CreateAPIView):
    serializer_class = MenuSerializer

    def post(self, request, *args, **kwargs):
        menu = get_object_or_404(Menu, pk=request.data.get('menu'))
        user = request.user
        vote, created = Vote.objects.get_or_create(user=user, menu=menu)

        if not created:
            vote.count += 1 
            vote.save()
        serializer = self.get_serializer(menu)

        return Response(serializer.data, status=status.HTTP_200_OK)
