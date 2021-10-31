"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import home_view, home_detail_view, post_list_view, create_post_view, post_action_view, delete_post_view,posts_list_view,posts_detail_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from accounts.views import logout_view,login_view,registration_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view), 
    path('create-post',create_post_view), #slash????????
    #path('posts/<int:post_id>/delete',delete_post_view),
    #path('posts/action', post_action_view),
    path('api/posts/<int:post_id>/', home_detail_view), # add path you want e.g. bla/ but don't delete '' above #int.. for dynamic routing
    path('posts/',post_list_view),
    path('api/posts/', include('posts.urls')), # i now have posts app as a rest api app (no longer django app)
    path('react/', TemplateView.as_view(template_name='react_via_django.html')),
    path('',posts_list_view),
    path('<int:post_id>/',posts_detail_view),
   # path('profile/<str:username>/',posts_profile_view),
    path('profile/',include('profiles.urls')),
    path('logout/',logout_view),
    path('login/',login_view),
    path('register/',registration_view),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

