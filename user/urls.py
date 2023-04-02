from django.urls import path
from user.views import home,Login_page,logout_user

urlpatterns =[
    path('',home,name = "user_home"),
    path('login/',Login_page,name="login"),
    path('logout/',logout_user,name="logout"),
]