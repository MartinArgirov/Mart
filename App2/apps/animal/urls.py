from django.urls import path
from .views import (home, about, AnimalCreateView, 
                   AnimalListView, AnimalDetailView, 
                   AnimalUpdateView, AnimalUpdateDetailView,
                   AnimalDeleteView, AnimalDeleteDetailView)

app_name = 'animal'

urlpatterns = [
    path('', home, name='home'), # Com espaço vazio é a pagina inicial
    path('about/', about, name='about'),
    path('novo/', AnimalCreateView.as_view(), name='novo'),
    path('lista/', AnimalListView.as_view(), name='lista'),
    path('detalhe/<int:pk>/', AnimalDetailView.as_view(), name='detalhe'),
    path('atualizar/<int:pk>/', AnimalUpdateView.as_view(), name='atualizar'),
    path('detalhe/atualizar/<int:pk>/', AnimalUpdateDetailView.as_view(), name='detalhe-atualizar'),
    path('eliminar/confirmar/<int:pk>/', AnimalDeleteView.as_view(), name='eliminar'),
    path('detalhe/eliminar/confirmar/<int:pk>/', AnimalDeleteDetailView.as_view(), name='detalhe-eliminar'),
    path('detalhe/atualizar/<int:pk>/', AnimalUpdateDetailView.as_view(), name='detalhe-eliminar'),
    path('atualizar/<int:pk>/', AnimalUpdateView.as_view(), name='atualizar'),
    path('confirmar/elimihar/<int:pk>/', AnimalDeleteView.as_view(), name='eliminar')
    
]