from rest_framework import serializers
from .models import Post
from django.conf import settings
from profiles.serializers import ProfileSerializer

ACTIONS=settings.ACTIONS
MAX_LEN = 200
class PostSerializer(serializers.ModelSerializer):
    likes=serializers.SerializerMethodField(read_only=True) #number, don't need to change it. use get likes?
    creator=ProfileSerializer(source='user.profile',read_only=True)

    class Meta:
        model=Post
        fields=['id', 'content', 'likes', 'creator','timestamp']
    def get_likes(self,obj):
        return obj.likes.count()

    def get_creator(self,obj):
        return obj.user.id # return id of user o later get that profile

    def validate_content(self, value):
        if len(value)>MAX_LEN:
            raise serializers.ValidationError('Too long')
        return value


class ActionsSerializer(serializers.Serializer): #not model?
    id=serializers.IntegerField() #required
    action=serializers.CharField() #required

    def validate_action(self, value):
        if not value in ACTIONS:
            raise serializers.ValidationError('Invalid action')
        return value