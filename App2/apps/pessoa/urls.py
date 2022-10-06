from django.urls import path
from .views import (contacts, about, email, PessoaCreateView, 
                    PessoaListView, PessoaDetailView, 
                    PessoaUpdateView, PessoaDeleteView,  PessoaUpdateDetailView)

app_name = 'pessoa'

urlpatterns = [
    path(' ', contacts, name='contacts'),# Com espaço vazio é a pagina inicial
    path('about/', about, name='about'),
    path('email/', email, name='email'),
    path('novo/', PessoaCreateView.as_view(), name='novo'),
    path('lista/', PessoaListView.as_view(), name='lista'),
    path('detalhe/<int:pk>/', PessoaDetailView.as_view(), name='detalhe'),
    path('atualizar/<int:pk>/', PessoaUpdateView.as_view(), name='atualizar'),
    path('confirmar/elimihar/<int:pk>/', PessoaDeleteView.as_view(), name='eliminar'),
    path('update/<int:pk>/', PessoaUpdateDetailView.as_view(), name='update')
]