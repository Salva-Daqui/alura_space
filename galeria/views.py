from django.shortcuts import render


def index(request):
    return render(request, 'galeria/exibition.html')

def img(request):
    return render(request, 'galeria/imagem.html')
