from django.urls import path
from rest_juego.views import agregarJ, controlJ, lista_juegos
from rest_juego.viewsLogin import login

urlpatterns = [
    path('lista_juegos/',lista_juegos,name="lista_juegos"),
    path('agregarJ/',agregarJ,name="agregarJ"),
    path('controlJ/<codigo>',controlJ,name="controlJ"),
    path('login/',login,name="login"),
]