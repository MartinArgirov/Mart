from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.pessoa.models import Pessoa

# Create your views here.
def contacts(request):
    return render(request, 'pessoa/contacts.html')

def about(request):
    return render(request, 'pessoa/about.html')

class PessoaCreateView(CreateView):
    model = Pessoa 
    fields = '__all__'
    success_url: reverse_lazy('pessoa:home')     