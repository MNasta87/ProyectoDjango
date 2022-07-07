from django.urls import path
from rest_juego.views import agregarJ, agregarP, agregarU, controlJ, controlP, controlU, lista_Publicaciones, lista_Usuarios, lista_juegos
from rest_juego.viewsLogin import login

urlpatterns = [
    path('lista_juegos/',lista_juegos,name="lista_juegos"),
    path('agregarJ/',agregarJ,name="agregarJ"),
    path('controlJ/<codigo>',controlJ,name="controlJ"),
    path('login/',login,name="login"),

    path('lista_Usuarios/',lista_Usuarios,name="lista_Usuarios"),
    path('agregarU/',agregarU,name="agregarU"),
    path('controlU/<codigo>',controlU,name="controlU"),

    path('lista_Publicaciones/',lista_Publicaciones,name="lista_Publicaciones"),
    path('agregarP/',agregarP,name="agregarP"),
    path('controlP/<codigo>',controlP,name="controlP"),

    
]