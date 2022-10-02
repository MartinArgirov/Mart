from django.urls import path
from .views import home, about, AnimalCreateView, AnimalListView, AnimalDetailView

app_name = 'animal'

urlpatterns = [
    path('', home, name='home'), # Com espaço vazio é a pagina inicial
    path('about/', about, name='about'),
    path('novo/', AnimalCreateView.as_view(), name='novo'),
    path('lista/', AnimalListView.as_view(), name='lista'),
    path('detalhe/<int:pk>/', AnimalDetailView.as_view(), name='detalhe')
]