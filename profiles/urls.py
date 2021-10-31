from .views import  profile_update_view, profile_detail_api_view, profile_detail_view
from django.urls import path


urlpatterns = [
    path('myprofile/edit', profile_update_view),
    path('<str:username>', profile_detail_view),
    path('api/<str:username>', profile_detail_api_view)  #profile/api/lea
]

