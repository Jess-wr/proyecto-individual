from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    imagen = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        label='Imagen:'
    )

    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'instrucciones', 'imagen']

        labels = {
            'titulo': 'Título de la receta',
            'ingredientes': 'Ingredientes',
            'instrucciones': 'Instrucciones para la receta',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la receta'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }
