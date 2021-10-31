from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name=serializers.SerializerMethodField(read_only=True) 
    last_name=serializers.SerializerMethodField(read_only=True) 
    username=serializers.SerializerMethodField(read_only=True) 
    email=serializers.SerializerMethodField(read_only=True) 

    class Meta:
        model=Profile
        fields=['location','about_me','timestamp','first_name','last_name','username','profile_image','email']
    
    def get_first_name(self,obj):
        return obj.user.first_name 

    def get_last_name(self,obj):
        return obj.user.last_name 

    def get_username(self,obj):
        return obj.user.username 

    def get_email(self,obj):
        return obj.user.email

