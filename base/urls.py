"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('divina-pagina-inicio',views.divina_pagina_inicio,name="divina_pagina_inicio"),
    path('la-voz-de-alfa-y-omega',views.omega, name="la_voz_de_alfa_y_omega"),
    path('crear-libros',views.crear_libros,name="crear-libros"),
    path('divina-pagina-inicio/<str:slug>',views.li2,name="sec"),
    path('search/', views.DevSearch.as_view(),name="search"),
    # path('projects/search',views.Search.as_view(), name="search"),
    
    
]
