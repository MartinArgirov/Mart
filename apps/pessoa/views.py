from django.shortcuts import render

# Create your views here.
def contacts(request):
    return render(request, 'pessoa/contacts.html')

def about(request):
    return render(request, 'pessoa/about.html')