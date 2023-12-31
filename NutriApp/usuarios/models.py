from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
CONTRASEÑA= re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

class UsuarioManager(models.Manager):
    def validar(self, postData):
        errors = {}
        if len(postData['nombre']) < 3:
            errors["nombre"] = "Nombre debe tener al menos 3 caracteres"
        if len(postData['apellido']) < 5:
            errors["apellido"] = "Apellido no puede tener menos de 5 caracteres"
        if self.filter(email=postData['email']).exists():
            errors["email"] = "Email ya existe."
        if postData['password'] != postData['confirmar_password']:
            errors["password"] = "Las contraseñas no coinciden"
        if not CONTRASEÑA.match(postData['password']):
            errors["confirmar_password"] = "La contraseña no es segura."

        return errors

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

