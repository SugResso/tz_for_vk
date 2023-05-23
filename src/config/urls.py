"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api_for_friends import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    # GET list friend-request-outgoing
    # POST create new friend-request-outgoing
    path('api/v1/users/<int:from_user>/friend-requests/outgoing/', views.FriendRequestsOutgoingAPIView.as_view()),

    # DELETE friend-request-outgoing
    path('api/v1/users/<int:from_user>/friend-requests/outgoing/<int:pk>/', views.FriendRequestsOutgoingAPIView.as_view()),

    # GET list friend-request-incoming
    path('api/v1/users/<int:to_user>/friend-requests/incoming/', views.FriendRequestsIncomingAPIView.as_view()),

    # DELETE/UPDATA list friend-request-incoming
    path('api/v1/users/<int:to_user>/friend-requests/incoming/<int:pk>/', views.FriendRequestsIncomingAPIView.as_view()),

    # GET list friends
    path('api/v1/users/<int:friend>/friends/', views.FriendsAPIView.as_view()),

    # DELETE friend
    path('api/v1/users/<int:friend>/friends/<int:pk>/', views.FriendsAPIView.as_view()),


    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
]
