from django.shortcuts import render, redirect
from django.contrib import messages
from recetas.models import Receta
import os
from django.core.paginator import Paginator
def index(request):
    recetas = Receta.objects.all().order_by('-created_at')  # Obtener todas las recetas ordenadas por fecha de publicación descendente
    # Configurar la paginación
    paginator = Paginator(recetas, 2)  # Muestra 2 recetas por página
    page = request.GET.get('page')  # Obtener el número de página desde la URL
    recetas_pagina = paginator.get_page(page)

    return render(request, 'index.html', {'recetas': recetas_pagina})