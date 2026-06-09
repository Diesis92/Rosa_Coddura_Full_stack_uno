from django.shortcuts import render
from django.views import View

from django.http import HttpResponse


#FBV
def home(request):
    return HttpResponse("Benvenuto nella Biblioteca!")

#CBV
class HomeView(View):
    def get(self, request):
        return HttpResponse("Benvenuto nella Biblioteca!") 

def lista_libri(request):
    return HttpResponse("Ecco la lista dei libri disponibili!") 


