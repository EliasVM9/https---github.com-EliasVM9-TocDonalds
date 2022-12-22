from django.shortcuts import render
from .models import Producto, Combo
from django.http import HttpResponse
from TocDonalds import *
def home(request):
    Combo = Producto.objects.all()
    return render(request, "inicio.html", {"Productos": Combo})
    #return HttpResponse("Hola Mundo")





