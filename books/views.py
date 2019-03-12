from django.shortcuts import render

# Create your views here.


def list_books(request):
    return render(request, 'index.html')
