# from django.test import TestCase
# from .models import Post
# from django.contrib.auth import get_user_model
# from rest_framework.test import APIClient
# import json

# # Create your tests here.

# User = get_user_model() # i want to test all urls -check documentation api-guide/testing/
# class PostTestCase(TestCase): #each function is 1 test
#     #each test case has method set up built into it. alows us to create all instances we need
#     def setUp(self): 
#         self.user=User.objects.create_user(username='testuser', password='topsecret') # add as many as you want
#         self.second_user=User.objects.create_user(username='testuser2', password='topsecret') # add as many as you want

#         Post.objects.create(content='testcontent2',user=self.user)
#         Post.objects.create(content='testcontent3',user=self.user)
#         Post.objects.create(content='testcontent4',user=self.user)
#         Post.objects.create(content='testcontent5',user=self.user)
#         self.currentCount = Post.objects.all().count()

#     def test_user_exists(self): #test_ at the begining, those are run
#         user=User.objects.get(username='testuser')
#         self.assertEqual(self.user.username, 'testuser')

#     def test_post_exists(self):
#         post=Post.objects.create(content='testcontent',user=self.user)
#         self.assertEqual(post.id, 5)
#         self.assertEqual(post.user, self.user)

#     def login(self, which_user):
#         client = APIClient()
#         client.login(username=which_user.username, password='topsecret')
#         return client

#     def test_login(self):
#         client = APIClient()
#         client.login(username=self.user.username, password='topsecret')
#         return client

#     def test_post_list(self):
#         # 1 created post in test database (look at setUp not post_exists)
#         client = self.login(self.user)
#         response=client.get('/api/posts/')
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(len(response.json()),4)


#     def test_liking(self):
#         client = self.login(self.user)
#         response_like=client.post('/api/posts/action',{'id':1,'action':'like'})  
#         like_num=response_like.json().get('likes')
#         self.assertEqual(response_like.status_code,200)
#         self.assertEqual(like_num,1)

#         response_dislike=client.post('/api/posts/action',{'id':1,'action':'dislike'})
#         like_num=response_dislike.json().get('likes')
#         self.assertEqual(response_dislike.status_code,200)
#         self.assertEqual(like_num,0)

#     def test_create_url(self):
#         client = self.login(self.user)
#         response=client.post('/api/posts/create',{'content':'bla'})
#         self.assertEqual(response.status_code,201)
#         self.assertEqual(response.json().get('content'),'bla')
#         self.assertEqual(response.json().get('likes'),0)
#         self.assertEqual(response.json().get('id'),self.currentCount+1)

#     def test_detail_view(self):
#         client = self.login(self.user)
#         response=client.get('/api/posts/1')
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response.json().get('id'),1)
 
#     def test_delete_view(self):
#         client = self.login(self.user)
#         client2 = self.login(self.second_user)

#         response_second_user=client2.delete('/api/posts/2/delete')
#         self.assertEqual(response_second_user.status_code,404)
#         self.assertEqual(response_second_user.json().get('message'),'Unauthorized')

#         response=client.delete('/api/posts/2/delete')
#         self.assertEqual(response.status_code,200)

#         response2=client.get('/api/posts/2')
#         self.assertEqual(response2.status_code,404)

