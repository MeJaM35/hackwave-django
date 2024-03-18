
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_user, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logoutUser, name='logout'),


    


    
]