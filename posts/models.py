from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class PostLike(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey('Post', on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    content = models.TextField(blank=True, null=True)
    #image = models.FileField(upload_to='images/', blank=True, null=True) #null e.g. if no picture dont show it
    user=models.ForeignKey(User, on_delete=models.CASCADE) # 1 post belogs to 1 user. user can have more posts. if owner is deleted all posts are deleted(SET_NULL or CASCADE or...)
    likes=models.ManyToManyField(User, related_name='post_user', blank=True, through=PostLike) #through model-for timestamp (can remove)
    timestamp=models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return{ #dict
            "id":self.id,
            "content":self.content,
            "likes":0,
        }
    class Meta:
        ordering=['-id'] #descending order
    
    def __str__(self): 
        return self.content