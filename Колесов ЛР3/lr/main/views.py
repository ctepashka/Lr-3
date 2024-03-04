from django.shortcuts import render


def index(request):
    return render(request, 'main/home.html')

def uslugi(request):
    return render(request, 'main/uslugi.html')

def address(request):
    return render(request, 'main/address.html')
