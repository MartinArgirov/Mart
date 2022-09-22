from django.urls import path
from .views import contacts, about, PessoaCreateView

app_name = 'pessoa'

urlpatterns = [
    path('', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('novo/', PessoaCreateView.as_view(), name= 'novo')
]