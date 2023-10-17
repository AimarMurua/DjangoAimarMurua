from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pertsona
from .models import Etxea
from .models import Alokairua


# Create your views here.

def index(request):
    pertsona = Pertsona.objects.all
    return render(request, 'index.html', {'pertsona':pertsona})

def etxeak(request):
    etxea = Etxea.objects.all
    return render(request, 'etxeak.html', {'etxea':etxea})

def gehitu(request):
    return render(request, 'gehitu.html')

def gehitupertsona(request):
    p_nan = request.POST['p_nan']
    p_izena = request.POST['p_izena']
    p_emaila = request.POST['p_emaila']

    pertsona = Pertsona(p_nan = p_nan, p_izena = p_izena, p_emaila = p_emaila)
    pertsona.save()
    return HttpResponseRedirect(reverse('index'))

def gehituetxea(request):
    return render(request, 'gehituetxea.html')

def gehituetxeaerregistroa(request):
    e_izena = request.POST['e_izena']
    e_herria = request.POST['e_herria']
    e_pertsonakopurua = request.POST['e_pertsonakopurua']

    etxea = Etxea(e_izena = e_izena, e_herria = e_herria, e_pertsonakopurua = e_pertsonakopurua)
    etxea.save()
    return HttpResponseRedirect(reverse('index'))

def ezabatu(request, p_nan):
    pertsona = Pertsona.objects.get(p_nan = p_nan)
    pertsona.delete()
    return HttpResponseRedirect(reverse('index'))

def ezabatuetxea(request, id):
    etxea = Etxea.objects.get(id = id)
    etxea.delete()
    return HttpResponseRedirect(reverse('index'))

def eguneratu(request, p_nan):
    pertsona = Pertsona.objects.get(p_nan = p_nan)
    return render(request, 'eguneratupertsona.html', {'pertsona':pertsona})

def eguneratuerregistroa(request, p_nan):
    p_nan = request.POST['p_nan']
    p_izena = request.POST['p_izena']
    p_emaila = request.POST['p_emaila']

    pertsona = Pertsona.objects.get(p_nan = p_nan)
    pertsona.p_nan = p_nan
    pertsona.p_izena = p_izena
    pertsona.p_emaila = p_emaila

    pertsona.save()
    return HttpResponseRedirect(reverse('index'))

def eguneratuetxea(request, id): 
    etxea = Etxea.objects.get(id = id)
    return render(request, 'eguneratuetxea.html', {'etxea':etxea})

def eguneratuetxeaerregistroa(request, id):
    e_izena = request.POST['e_izena']
    e_herria = request.POST['e_herria']
    e_pertsonakopurua = request.POST['e_pertsonakopurua']

    etxea = Etxea.objects.get(id = id)
    etxea.e_izena = e_izena
    etxea.e_herria = e_herria
    etxea.e_pertsonakopurua = e_pertsonakopurua

    etxea.save()
    return HttpResponseRedirect(reverse('index'))

def alokairua(request):
    alokairua = Alokairua.objects.all
    return render(request, 'alokairuak.html', {'alokairua':alokairua})

def gehitualokairua(request):
    pertsona = Pertsona.objects.all
    etxea = Etxea.objects.all

    return render(request, 'gehitualokairua.html', {'pertsona':pertsona, 'etxea':etxea})

def gehitualokairuaerregistroa(request):
    etxea = request.POST['etxea_izena']
    etxeaOk = Etxea.objects.get(e_izena = etxea)

    pertsona = request.POST['pertsona_izena']
    pertsonaOk = Pertsona.objects.get(p_izena = pertsona)

    alokairudatahasiera = request.POST['alokairu_data_hasiera']
    alokairudataamaiera = request.POST['alokairu_data_amaiera']

    alokairua = Alokairua(etxea_izena = etxeaOk, pertsona_izena = pertsonaOk, alokairu_data_hasiera = alokairudatahasiera, alokairu_data_amaiera = alokairudataamaiera)

    alokairua.save()
    return HttpResponseRedirect(reverse('index'))