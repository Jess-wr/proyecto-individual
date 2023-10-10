from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Receta
from .forms import RecetaForm
import os
from django.core.paginator import Paginator
def inicio(request):
    recetas = Receta.objects.all().order_by('-created_at')  # Obtener todas las recetas ordenadas por fecha de publicación descendente
    # Configurar la paginación
    paginator = Paginator(recetas, 2)  # Muestra 2 recetas por página
    page = request.GET.get('page')  # Obtener el número de página desde la URL
    recetas_pagina = paginator.get_page(page)

    return render(request, 'recetas/recetas.html', {'recetas': recetas_pagina})


def agregar_receta(request):
    if request.method == 'POST':
        usuario_id = request.session['usuario']['id']
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.usuario_id = usuario_id
            receta.save()
            return redirect('inicio')
    else:
        form = RecetaForm()
    return render(request, 'recetas/form_receta.html', {'form': form})

def editar_receta(request, id):
    receta = Receta.objects.get(id=id)
    if request.method == 'POST':
        # Rellena el formulario con los datos del POST y la instancia de la receta
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            messages.success(request, "La receta ha sido actualizada correctamente.")
            return redirect('inicio')
    else:
        form = RecetaForm(instance=receta)

    return render(request, 'recetas/editar_receta.html', {'form': form, 'receta': receta})


def eliminar_receta(request, id):
    
    receta = Receta.objects.get(id=id)
    # Obtener la ruta de la imagen relacionada
    ruta_imagen = receta.imagen.path
    receta.delete()
    # Eliminar la imagen relacionada
    if os.path.exists(ruta_imagen):
        os.remove(ruta_imagen)

    return redirect('inicio')