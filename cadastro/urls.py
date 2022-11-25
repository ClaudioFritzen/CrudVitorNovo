from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name="menu"),
     path("check_user/", views.check_user, name="check_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("update_user/", views.update_user, name="update_user"),
    
]
