from django.urls import path
from .views import contacts, about

app_name = 'pessoa'

urlpatterns = [
    path('', contacts, name='contacts'),
    path('about/', about, name='about')
]