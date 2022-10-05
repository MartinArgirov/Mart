from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Despesa

# Apresentação de página estática
def home(request):
    return render(request, 'despesas/home.html')

def about(request):
    return render(request, 'despesas/about.html')
# Create your views here.
class DespesaCreateView(CreateView):
    model = Despesa # atributo
    fields = '__all__' # atributo que mostra Nome, Especie , Idade em Animal
    #success_url = reverse_lazy('animal:home')
    success_url = reverse_lazy('despesa:lista')  

class DespesaListView(ListView):
    model = Despesa

class DespesaDetailView(DetailView):
    model = Despesa 

class DespesaUpdateView(UpdateView):
    model = Despesa
    fields = ['valor', 'categoria', 'mes']
    template_name = 'despesas/despesa_update.html'
    success_url = reverse_lazy('despesa:lista') 

class DespesaUpdateDetailView(UpdateView):
    model = Despesa
    fields = ['valor', 'categoria', 'mes']
    template_name = 'despesas/despesa_update.html'
    success_url = reverse_lazy('despesa:lista')
    
    def get_success_url(self):
        return reverse('despesa:detalhe', kwargs={'pk': self.object.id})

class DespesaDeleteView(DeleteView):
    model = Despesa
    #template_name = 'control_despesa/despesa_detail_confirm_delete.html'
    success_url = reverse_lazy('despesa:lista')

class DespesaDeleteDetailView(DeleteView):
    model = Despesa
    template_name = 'despesas/despesa_detail_confirm_delete.html'
    success_url = reverse_lazy('despesa:lista')                                   