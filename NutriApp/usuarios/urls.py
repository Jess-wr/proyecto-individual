from django.urls import path
from . import views
from principal import views as principal_views

urlpatterns = [
    path('', principal_views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'),
]
