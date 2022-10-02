from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from apps.pessoa.models import Pessoa

# Create your views here.
def contacts(request):
    return render(request, 'pessoa/contacts.html')

def about(request):
    return render(request, 'pessoa/about.html')

def email(request):
    return render(request, 'pessoa/email.html')    
# Create your views here.
class PessoaCreateView(CreateView):
    model = Pessoa 
    fields = '__all__'
    #success_url = reverse_lazy('pessoa:home')
    success_url = reverse_lazy('pessoa:lista')

class PessoaListView(ListView):
    model = Pessoa

class PessoaDetailView(DetailView):
    model = Pessoa    