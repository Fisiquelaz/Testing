from django import forms
from .models import Entrega
class FormEntrega(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['nome','rua','bairro','numeroCasa','complemento','qtd']