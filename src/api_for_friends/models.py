from django.contrib.auth.models import User
from django.db import models


class FriendRequest(models.Model):
    class Meta:
        verbose_name_plural = 'Заявки в друзья'

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_user} --> {self.to_user}"


class Friend(models.Model):
    class Meta:
        verbose_name_plural = 'Друзья'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} <--> {self.friend}"
