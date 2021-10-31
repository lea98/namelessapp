from rest_framework import authentication
from django.contrib.auth import get_user_model

User=get_user_model()


class DevAuthentication(authentication.BasicAuthentication):
    def authenticate(self,request):
        qs=User.objects.filter(id=1)
        user=qs.order_by('?').first() #random user
        return (user,None)