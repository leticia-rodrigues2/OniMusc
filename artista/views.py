import xlwt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Musica
from.models import Artista
from.form import MusicaForm
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook


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

def update(request, pk):
    data = {}
    musica = Musica.objects.get(pk=pk)
    form = MusicaForm(request.POST or None, instance=musica)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['musica']= musica
    return render(request, 'artista/form.html', data)


def delete(request, pk):
    musica= Musica.objects.get(pk=pk)
    musica.delete()
    return redirect('url_listagem')

def excel(request):
    idArtista = request.POST['artista']
    workbook = Workbook()
    worksheet = workbook.active

    artista = Artista.objects.get(pk=idArtista)
    musicas= artista.musicas.all()

    # preencher cabeçalho
    worksheet['A' + str(1)] = "Nome do artista"
    worksheet['B' + str(1)] = "Nome da musica"


    #preencher corpo da planilha
    i=2
    for musica in musicas:
        worksheet['A' + str(i)] = musica.artista.nome
        worksheet['B' + str(i)] = musica.nome
        i+=1
    response = HttpResponse(content=save_virtual_workbook(workbook))#, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=myexport.xlsx'
    return response

def relatorioArtista(request):
    data = {}
    artistas = Artista.objects.all()
    data['artistas'] = artistas
    return render(request, 'artista/relatorio.html', data)

