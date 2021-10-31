from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
# Create your views here.

def login_view(request,*args,**kwargs): 
    form=AuthenticationForm(request,data=request.POST or None) #for this form we need to pass also request
    if form.is_valid(): # django auth form (not standard form)
        user_=form.get_user()
        login(request,user_)
        return redirect('/') #home page
    return render(request,'accounts/autenticate.html',{'form':form,'button_text':'Login','title':'Welcome! Please login','navbar':'login'}) #we need context


def registration_view(request,*args,**kwargs): 
    form=UserCreationForm(request.POST or None)
    if form.is_valid(): # django auth form (not standard form)
        user=form.save(commit=True)
        user.set_password(form.cleaned_data.get('password1')) # user has to repear pass so i have 2
        return redirect('/login')
    return render(request,'accounts/autenticate.html',{'form':form,'button_text':'Register','title':'Register','navbar':'reg'}) #we need context

def logout_view(request,*args,**kwargs): 
    if request.method=='GET':
        logout(request)
    return redirect('/login')
    #return render(request,'accounts/autenticate.html',{'form':None,'button_text':'Logout','title':'Logout'}) 