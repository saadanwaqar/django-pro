from django_onesignal.client import OnesignalClient
from django.shortcuts import render,HttpResponse
from . models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')

def li2(request,slug):
    article = Divina_Pagina.objects.filter(slug=slug).first()
    return render(request,'divina-list.html',{'article':article})

def divina_pagina_inicio(request):
    docs = Divina_Pagina.objects.all()
   
    print(docs)
    return render(request, 'divina-pagina-inicio.html',{'docs':docs})

def omega(request):
    return render(request, 'la-voz-de-alfa-y-omega.html')

def crear_libros(request):
    return render(request, 'crear-libros.html')

from django.views import View 

class DevSearch(View):
    def get(self,request ):
        queryset = request.GET.get('queryset',None) 
        allpostTitle = Divina_Pagina.objects.filter(desc__icontains=queryset) 
        allpostDesc = Divina_Pagina.objects.filter(slug=queryset) 
         
        allpost= allpostTitle.union(allpostDesc) 
         
        return render(request,'search.html',{'items':allpostTitle,'query':queryset} )
    

# client = OnesignalClient()

# # set up your credentials. rest_api_key is not required for all API calls
# client.set_app_id( app_id=APP_ID , rest_api_key=REST_API_KEY):


# # Pass the TITLE the CONTENT of the push notificaiton
# # Pass 1 or more ids in a **List** objet
# client.create_message(self, title=TITLE, cont=CONTENT, ids:[ID]):


# # Check on Onesignal documentation if the notification you are sending requires the `rest_api_key`
# response = client.send_message(requires_rest_api_key=BOOL)

# print(response.status)
# print(response.body)