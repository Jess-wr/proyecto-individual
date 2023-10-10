from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
import bcrypt
def inicio(request):
    return render(request, 'usuarios/inicio.html')
def registro(request):
    if request.method == 'GET':

        if 'usuario' in request.session:
            messages.warning(request,"Ya estás registrado.")
            return redirect("/acceso/inicio")


        context = {}
        return render(request, 'usuarios/registro.html', context)

    if request.method == 'POST':
        # Llama a la función validar del UsuarioManager
        errores = Usuario.objects.validar(request.POST)

        if errores:
            # Si hay errores de validación, muestra un mensaje de error y vuelve al formulario
            for error in errores.values():
                messages.error(request, error)
            return redirect("/acceso/registro")

        pass_encriptada = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(f"la contraseña '{request.POST['password']}' con bcrypt quedo en: {pass_encriptada}")

        user = Usuario.objects.create(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            email = request.POST['email'],
            password = pass_encriptada,
        )


        usuario_session = {
            'id' : user.id,
            'nombre' : user.nombre + ' ' + user.apellido,
            'email' : user.email,
        }

        print(usuario_session)
        request.session['usuario'] = usuario_session

        messages.success(request, "Usuario creado exitosamente.")
        return redirect("/acceso/login")

def login(request):
    if request.method == 'GET':

        if 'usuario' in request.session:
            messages.warning(request,"Ya iniciaste Sesion")
            return redirect("/acceso/inicio")

        context = {}
        return render(request, 'usuarios/login.html', context)

    if request.method == 'POST':
        usuarios = Usuario.objects.filter(email=request.POST['email']) 
        if usuarios: 
            usuario = usuarios[0] 
            print(usuario)

            if bcrypt.checkpw(request.POST['password'].encode(), usuario.password.encode()):

                usuario_session = {
                    'id' : usuario.id,
                    'nombre' : usuario.nombre + ' ' + usuario.apellido,
                    'email' : usuario.email,
                }

                print('El usuario de la sesion', usuario_session)
                request.session['usuario'] = usuario_session
                messages.success(request, "Haz iniciado sesion!")
                return redirect('/acceso/inicio')
            else:
                messages.error(request, "La contraseña o el correo no coinciden")
                return redirect("/acceso/login")

        else:
            messages.error(request,"El correo o la contraseña indicado no existe")
            return redirect("/acceso/login")
        
def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']

    return redirect("/acceso/login")

