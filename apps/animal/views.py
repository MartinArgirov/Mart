from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Animal

# Apresentação de página estática
def home(request):
    return render(request, 'animal/home.html')

def about(request):
    return render(request, 'animal/about.html')
# Create your views here.
class AnimalCreateView(CreateView):
    model = Animal # atributo
    fields = '__all__' # atributo que mostra Nome, Especie , Idade em Animal
    #success_url = reverse_lazy('animal:home')
    success_url = reverse_lazy('animal:lista')  

class AnimalListView(ListView):
    model = Animal     