from django.shortcuts import render, redirect
from django.http import Http404
from .models import Profile
# Create your views here.
from .forms import ProfileForm
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def profile_detail_api_view(request,username,*args,**kwargs):

    qs=Profile.objects.filter(user__username=username)
    if not qs.exists():
        raise Http404
    obj=qs.first() 
    
    data=ProfileSerializer(instance=obj)
    return Response(data.data,status=200)



def profile_detail_view(request,username,*args,**kwargs):

    qs=Profile.objects.filter(user__username=username)
    if not qs.exists():
        raise Http404
    obj=qs.first() 

    data=ProfileSerializer(instance=obj)
    return render(request,'profiles/detail.html',{'username':username, 'profile':obj})


def profile_update_view(request,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect ('/login')
    # one on one, mz actual instance
    form=ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form=ProfileForm(request.POST or None,request.FILES, instance=request.user.profile)
        obj=form.save(commit=False)
        first_name=form.cleaned_data.get('first_name')        
        last_name=form.cleaned_data.get('last_name')
        email=form.cleaned_data.get('email')

        request.user.first_name=first_name
        request.user.last_name=last_name
        request.user.email=email

        request.user.save()
        obj.save()
        return redirect(f'/profile/{request.user}')
    return render (request,'profiles/form.html',{'form':form,'button_text':'Confirm', 'navbar':'edit'})