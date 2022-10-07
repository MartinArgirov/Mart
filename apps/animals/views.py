from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Animals

# Apresentação de página estática
def home(request):
    return render(request, 'animals/home.html')

def about(request):
    return render(request, 'animals/about.html')
# Create your views here.
class AnimalsCreateView(CreateView):
    model = Animals # atributo
    fields = '__all__' # atributo que mostra Nome, Especie , Idade em Animal
    #success_url = reverse_lazy('animals:home')
    success_url = reverse_lazy('animals:lista')  

class AnimalsListView(ListView):
    model = Animals

class AnimalsDetailView(DetailView):
    model = Animals 

class AnimalsUpdateView(UpdateView):
    model = AnimalsListView
    fields = ['nome', 'idade', 'pessoa']
    template_name = 'animals/animals_update.html'
    success_url = reverse_lazy('animal:lista') 

class AnimalsUpdateDetailView(UpdateView):
    model = Animals
    fields = ['nome', 'idade', 'pessoa']
    template_name = 'animals/animals_detail_update.html'
    #success_url = reverse_lazy('animals:lista')
    
    def get_success_url(self):
        return reverse('animals:detalhe', kwargs={'pk': self.object.id})

class AnimalsDeleteView(DeleteView):
    model = Animals
    template_name = 'animals/animals_detail_confirm_delete.html'
    success_url = reverse_lazy('animals:lista')

class AnimalsDeleteDetailView(DeleteView):
    model = Animals
    template_name = 'animals/animals_detail_confirm_delete.html'
    success_url = reverse_lazy('animals:lista')