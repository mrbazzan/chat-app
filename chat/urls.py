
from django.urls import path, re_path
from . import views


urlpatterns = [

    path('checkview', views.check_view, name="checkview"),
    path('send', views.send, name="send"),
   
    path('', views.home, name="home"),
    path('<str:room>/', views.room, name="room"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),

]