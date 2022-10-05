from django.urls import path
from .views import (home, about, DespesaCreateView, 
                   DespesaListView, DespesaDetailView, 
                   DespesaUpdateView, DespesaUpdateDetailView,
                   DespesaDeleteView, DespesaDeleteDetailView)

app_name = 'despesas'

urlpatterns = [
    path('', home, name='home'), # Com espaço vazio é a pagina inicial
    path('about/', about, name='about'),
    path('novo/', DespesaCreateView.as_view(), name='novo'),
    path('lista/', DespesaListView.as_view(), name='lista'),
    path('detalhe/<int:pk>/', DespesaDetailView.as_view(), name='detalhe'),
    path('atualizar/<int:pk>/', DespesaUpdateView.as_view(), name='atualizar'),
    path('detalhe/atualizar/<int:pk>/', DespesaUpdateDetailView.as_view(), name='detalhe-atualizar'),
    path('eliminar/confirmar/<int:pk>/', DespesaDeleteView.as_view(), name='eliminar'),
    path('detalhe/eliminar/confirmar/<int:pk>/', DespesaDeleteDetailView.as_view(), name='detalhe-eliminar'),
    path('detalhe/atualizar/<int:pk>/', DespesaUpdateDetailView.as_view(), name='detalhe-eliminar'),
    path('atualizar/<int:pk>/', DespesaUpdateView.as_view(), name='atualizar'),
    path('confirmar/elimihar/<int:pk>/', DespesaDeleteView.as_view(), name='eliminar')
    
]