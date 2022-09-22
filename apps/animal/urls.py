from django.urls import path
from .views import home, about, AnimalCreateView

app_name = 'animal'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('novo/', AnimalCreateView.as_view(), name= 'novo')
]