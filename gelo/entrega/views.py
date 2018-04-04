from django.shortcuts import render,redirect
from .models import Entrega
from .forms import FormEntrega

# Create your views here.
def home(request):
    return render(request, "home.html")


def listaEntregas(request):
    entregas = Entrega.objects.all()
    return render(request, 'entregas.html', {'entregas': entregas})


def salvar(request):
    form = FormEntrega(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listaEntregas')
    return render(request,'formEntregas.html',{'form':form})