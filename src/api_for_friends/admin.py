from django.contrib import admin
from api_for_friends.models import FriendRequest, Friend


# Register your models here.
@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class Friend(admin.ModelAdmin):
    pass
