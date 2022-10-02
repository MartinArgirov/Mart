from django.urls import path
from .views import contacts, about, email,  PessoaCreateView, PessoaListView, PessoaDetailView

app_name = 'pessoa'

urlpatterns = [
    path('', contacts, name='contacts'),# Com espaço vazio é a pagina inicial
    path('about/', about, name='about'),
    path('email/', email, name='email'),
    path('novo/', PessoaCreateView.as_view(), name='novo'),
    path('lista/', PessoaListView.as_view(), name='lista'),
    path('detalhe/<int:pk>/', PessoaDetailView.as_view(), name='detalhe')
]