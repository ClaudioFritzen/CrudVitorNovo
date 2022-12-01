from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name="menu"),
     path("check_user/", views.check_user, name="check_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("update_user/delete/<int:id>", views.delete, name='delete'),
    path("update_user/", views.update_user, name="update_user"),
    path('update_user/update/<int:id>', views.update, name='update'),
    #path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('update_user/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),  

]
