from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api_for_friends.models import FriendRequest
from api_for_friends.serializers import UserSerializer, FriendRequestsSerializer, FriendSerializer


# Create your views here.
# User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# End User


# FriendRequests
class FriendRequestsOutgoingAPIView(APIView):
    serializer_class = FriendRequestsSerializer
    model = FriendRequest
    """
    Вынести в миксин

    Добавить условие: по проверке уникальности заявки, по проверки встречной заявки
    """

    def get(self, request, *args, **kwargs):
        """Получить список исходящих заявок в друзья"""
        from_user = kwargs.get('from_user', None)
        if not from_user:
            return Response({'error': 'Method GET not allowed'})
        queryset = self.model.objects.filter(from_user=from_user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """Создать заявку в друзья"""

        # Есть ли уже такая запись
        if self.model.objects.filter(from_user=request.data['from_user'], to_user=request.data['to_user']):
            return Response({'error': 'This entry already exists'})

        # Если есть обратная запись, то добавляем в друзья(accepted=True)
        if self.model.objects.filter(from_user=request.data['to_user'], to_user=request.data['from_user']):
            # instance = self.model.objects.filter(
            #     Q(from_user=request.data['to_user'], to_user=request.data['from_user']) | Q(
            #         from_user=request.data['from_user'], to_user=request.data['to_user']))

            instance = self.model.objects.filter(from_user=request.data['to_user'], to_user=request.data['from_user'])[0]

            serializer = self.serializer_class(instance=instance, data={'accepted': True}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = dict()
            for i, j in request.data.items():
                data[i] = j
            data['accepted'] = True

            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """Отменить заявку в друзья"""
        from_user = kwargs.get('from_user', None)
        pk = kwargs.get('pk', None)

        if not from_user or not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = self.model.objects.filter(from_user=from_user).get(id=pk)
        except:
            return Response({'error': 'Object does not exists'})

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FriendRequestsIncomingAPIView(APIView):
    serializer_class = FriendRequestsSerializer
    model = FriendRequest

    def get(self, request, *args, **kwargs):
        """Получить список входящих заявок в друзья"""
        to_user = kwargs.get('to_user', None)
        if not to_user:
            return Response({'error': 'Method GET not allowed'})
        queryset = self.model.objects.filter(to_user=to_user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """Отменить заявку в друзья"""
        to_user = kwargs.get('to_user', None)
        pk = kwargs.get('pk', None)

        if not to_user or not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = self.model.objects.filter(to_user=to_user).get(id=pk)
        except:
            return Response({'error': 'Object does not exists'})

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# End FriendRequests


# Friend
class FriendsAPIView(APIView):
    serializer_class = FriendRequestsSerializer
    model = FriendRequest

    """
    
    """

    def get(self, request, *args, **kwargs):
        """Получить список друзей"""
        friend = kwargs.get('friend', None)
        if not friend:
            return Response({'error': 'Method GET not allowed'})
        queryset = self.model.objects.filter(from_user=friend, accepted=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """Отменить заявку в друзья"""
        friend = kwargs.get('friend', None)
        pk = kwargs.get('pk', None)

        if not friend or not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = self.model.objects.filter(from_user=friend).get(id=pk)
        except:
            return Response({'error': 'Object does not exists'})

        instance_update = self.model.objects.filter(from_user=instance.to_user_id, to_user=instance.from_user_id)[0]

        serializer = self.serializer_class(instance=instance_update, data={'accepted': False}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# End Friend
