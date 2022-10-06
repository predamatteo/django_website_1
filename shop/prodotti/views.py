from django.shortcuts import render
from django.http import HttpResponse
from .models import Prodotto

def index(request):
    #return HttpResponse('Pagina dei Prodotti')
    prodotti = Prodotto.objects.all()
    #il metodo .object.all() prodotto eredita dalla classe models.Models che contiene
    #metodi per accedere agli attributi della classe
    return render(request,'index.html',{'prodotti':prodotti})

def in_offerta(request):
    prodotti = Prodotto.objects.all()
    return render(request,'in_offerta.html',{'prodotti':prodotti})

def contattaci(request):
    return render(request,'contattaci.html')
