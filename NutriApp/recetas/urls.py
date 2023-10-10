from django.urls import path
from . import views

urlpatterns = [
    path('agregar_receta/', views.agregar_receta, name='agregar_receta'),
    path('lista/', views.inicio, name='inicio'),
    path('receta/editar/<int:id>/', views.editar_receta, name='editar_receta'),
    path('eliminar_receta/<int:id>/', views.eliminar_receta, name='eliminar_receta'),
]