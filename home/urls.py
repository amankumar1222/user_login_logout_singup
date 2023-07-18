from django.urls import path 
from .import views

urlpatterns = [
    path("user/" ,views.index, name="home"),
    path("login/" ,views.loginUser, name="login"),
    path("logout/" ,views.logoutUser, name="logout"),
    path("singup/" ,views.singupUser, name="singup"),
]

