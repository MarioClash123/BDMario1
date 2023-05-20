from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import cliente
from .forms import ClienteForm
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def cliente_views(request):
    clientes = cliente.objects.all()
    print(clientes)
    return render(request, 'cliente/index.html', {'clientes': clientes})

def crear(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cliente')
    return render(request, 'cliente/crear.html', {'formulario':formulario})

def editar(request, id):
    clientes = cliente.objects.get(id=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=clientes)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('cliente')
    return render(request, 'cliente/editar.html', {'formulario':formulario})

def eliminar(request, id):
    clientes = cliente.objects.get(id=id)
    clientes.delete()
    return redirect('cliente')