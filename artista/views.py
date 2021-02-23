
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Musica
from.models import Artista
from.form import MusicaForm


import datetime

def home(request):
    data = {}

    return render(request, 'artista/home.html',data)

def listagem(request):
    data = {}

    data['musicas'] = Musica.objects.all()
    return render(request, 'artista/listagem.html', data)


def nova_musica (request):
    data={}
    form=MusicaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form']=form
    return render(request, 'artista/form.html', data)



