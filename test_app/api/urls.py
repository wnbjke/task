from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserUpdate.as_view()),
    path('users_delete/<int:pk>/', UserDestroy.as_view()),
    path('restaurant/', RestaurantList.as_view()),
    path('restaurant/<int:pk>/', RestaurantUpdate.as_view()),
    path('restaurant_delete/<int:pk>/', RestaurantDestroy.as_view()),
    path('menu/', MenuList.as_view()),
    path('menu/vote/', MenuVoteView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_obtain_pair'),
]
