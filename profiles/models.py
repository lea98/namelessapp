from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.
#one to one field
#1 profile associated to 1 user
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location=models.CharField(max_length=50,null=True, blank=True)
    about_me=models.TextField(null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    profile_image=models.ImageField(null=True,blank=True,default='')#???
    #email_address=models.CharField(max_length=50,null=True, blank=True)


# django has built in method signals-if there is action in database signal can be sent out
def user_did_save(sender,instance,created,*args,**kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(user_did_save,sender=settings.AUTH_USER_MODEL)

#post save allows to define method user did save. in that i can create new profile
# signal knows what obj am I tracking here(user itself)
#user after its save it will trigger this function?