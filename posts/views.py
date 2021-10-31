from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect # added
from .models import Post #relative import (in same folder)
from .forms import PostForm
from django.utils.http import is_safe_url
from django.conf import settings
from .serializers import PostSerializer, ActionsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

allowed_hosts=settings.ALLOWED_HOSTS
# Create your views here.

def home_view(request, *args, **kwargs): #user none?
    #print(args, kwargs) # {'post_id': 12} if request is bla/12, dictionary
    return render(request, "pages/home.html", context={'navbar': 'home'}, status=200)


# def home_detail_view_old(request, post_id, *args, **kwargs):
#    # print(args, kwargs) # {'post_id': 12} if request is bla/12, dictionary
#     # REST API VIEW
#     data = { #dict
#         "id": post_id,
#         #"image_path": obj.image.url
#     }
#     status = 200
#     try:
#         obj = Post.objects.get(id=post_id)
#         #if there is an object add content
#         data['content'] = obj.content
#     except:
#         data['message'] = 'Not found sorry'
#         status = 404

#     return JsonResponse(data, status=status)
#     #return HttpResponse(f"<h1>Hello World. This is {post_id} and {obj.content}</h1>") in except there was raise Http404
#      # it returns dynamic content. e.g. based on id, but we want to return content stored in db. import posts from models


# def post_list_view_old(request, *args, **kwargs):
#     # REST API VIEW
#     qs=Post.objects.all()   #queryset-list django model objects
#    # posts_list = [{"id":x.id, "content":x.content, "likes_num":0} for x in qs] #  is list - to itarate throug use dict
#    #added dict to serialize in models
#     posts_list=[x.serialize() for x in qs]
#     data={
#         "isUser":False,
#         "response": posts_list
#     }
#     return JsonResponse(data)

# def create_post_view_old(request, *args, **kwargs): 
#     user=request.user
#     if not request.user.is_authenticated: # else i'll only get 500 server error
#         user=None
#         if request.is_ajax():
#             return JsonResponse({}, status=401) #401-unauthorized 403 change?
#         return redirect(settings.LOGIN_URL) #from django
#    # print("test",request.is_ajax())
#     form=PostForm(request.POST or None)
#     next_url=request.POST.get('next') or None # to not do redirect but stay on page after creating post
#     if form.is_valid():
#         obj=form.save(commit=False)

#         obj.user=request.user # no need for or None because of first if block. also I didn't add null=True in user Posts

#         obj.save()
#         if request.is_ajax():
#             return JsonResponse(obj.serialize(),status=201)#created items

#         if next_url and is_safe_url(next_url, allowed_hosts):     #django has ways for safe redirecting
#             return redirect(next_url)
#         form=PostForm()
#     if form.errors:
#         if request.is_ajax():
#             return JsonResponse(form.errors,status=400)
#     return render(request, 'components/forms.html', context={"form":form})

#############################################################################################
#@authentication_classes([SessionAuthentication]) #only for session auth, user or another appx
@api_view(['POST'])  #decorator-pass list of methods I want to support
@permission_classes([IsAuthenticated]) #permission to do anything with this view
def create_post_view(request, *args, **kwargs): 
    serializer=PostSerializer(data=request.data) #different than forms, need to pass data=... dont use request.POST but data
    if serializer.is_valid(raise_exception=True): #no need to think about error?
        serializer.save(user=request.user) 
        return Response(serializer.data, status=201) #instead of json
    return Response({}, status=400)

@api_view(['GET'])
def post_list_view(request, *args, **kwargs): 
    qs=Post.objects.all()  
    username=request.GET.get('username') #url will pass param as ?username=.. important for profile(to show only my posts)
    if username!=None:
        qs=qs.filter(user__username__iexact=username) #exact for capital letters etc
    serializer=PostSerializer(qs,many=True)

    return Response(serializer.data,status=200)

@api_view(['GET'])
def home_detail_view(request, post_id, *args, **kwargs):
    qs=Post.objects.filter(id=post_id) #url e.g. posts/2
    if not qs.exists():
        return Response({},status=404)
    obj=qs.first()
    serializer=PostSerializer(obj)
    return Response(serializer.data,status=200)


@api_view(['POST','DELETE']) 
@permission_classes([IsAuthenticated])
def delete_post_view(request, post_id, *args, **kwargs): #checks permisiion that this user can delete this and its on server side
    qs=Post.objects.filter(id=post_id) #url e.g. posts/2
    if not qs.exists():
        return Response({},status=404)
    qs=qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message":'Unauthorized'},status=404)
    obj=qs.first()
    obj.delete()
    return Response({"message":'Deleted'},status=200)

@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def post_action_view(request, *args, **kwargs): #allow any user to like any post (actions:like, unlike, retweet)
    serializer=ActionsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data=serializer.validated_data
        post_id=data.get('id')
        action=data.get('action')

        qs=Post.objects.filter(id=post_id) 
        if not qs.exists():
            return Response({},status=404)

        obj=qs.first()
        # if request.user in obj.likes.all():
        #     obj.likes.remove(request.user)
        # else:
        #     obj.likes.add(request.user)
        if action=='like':
            obj.likes.add(request.user)
            serializer = PostSerializer(obj) #?
            return Response(serializer.data, status=200)
        elif action=='dislike':
            obj.likes.remove(request.user)
            serializer = PostSerializer(obj) #?
            return Response(serializer.data, status=200)
        #elif action == add actions
    return Response({"message":'Liked'},status=200)



    #new views to render actual http (not from standard views)

def posts_list_view(request, *args, **kwargs):
 
    return render(request, "posts/list.html")


def posts_detail_view(request, post_id, *args, **kwargs):

    return render(request, "posts/detail.html", context={'id':post_id})

    
# def posts_profile_view(request,username, *args, **kwargs):

#     return render(request, "posts/profile.html", context={'username':username})


