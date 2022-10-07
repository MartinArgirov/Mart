from django.urls import path
from .views import (home, about, AnimalsCreateView, 
                   AnimalsListView, AnimalsDetailView, 
                   AnimalsUpdateView, AnimalsUpdateDetailView,
                   AnimalsDeleteView, AnimalsDeleteDetailView)

app_name = 'animals'

urlpatterns = [
    path('', home, name='home'), # Com espaço vazio é a pagina inicial
    path('about/', about, name='about'),
    path('novo/', AnimalsCreateView.as_view(), name='novo'),
    path('lista/', AnimalsListView.as_view(), name='lista'),
    path('detalhe/<int:pk>/', AnimalsDetailView.as_view(), name='detalhe'),
    path('atualizar/<int:pk>/', AnimalsUpdateView.as_view(), name='atualizar'),
    path('detalhe/atualizar/<int:pk>/', AnimalsUpdateDetailView.as_view(), name='detalhe-atualizar'),
    path('eliminar/confirmar/<int:pk>/', AnimalsDeleteView.as_view(), name='eliminar'),
    path('detalhe/eliminar/confirmar/<int:pk>/', AnimalsDeleteDetailView.as_view(), name='detalhe-eliminar'),
    path('detalhe/atualizar/<int:pk>/', AnimalsUpdateDetailView.as_view(), name='detalhe-eliminar'),
    path('atualizar/<int:pk>/', AnimalsUpdateView.as_view(), name='atualizar'),
    path('confirmar/elimihar/<int:pk>/', AnimalsDeleteView.as_view(), name='eliminar')
    
]