from django.contrib import admin
from django.urls import path
from .views import home_view, home_detail_view, post_list_view, create_post_view, post_action_view, delete_post_view
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', home_view), 
    path('',post_list_view), 
    path('<int:post_id>', home_detail_view), # add path you want e.g. bla/ but don't delete '' above #int.. for dynamic routing
    path('create',create_post_view),
    path('<int:post_id>/delete',delete_post_view),
    path('action', post_action_view),

]
