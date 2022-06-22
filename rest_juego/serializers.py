
from rest_framework import serializers
from PrayTheNews.models import Juego

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['idJuego','tituloJuego','textoJuego','precioJuego'
                    ,'linkJuego','plataforma']

class JuegoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['idJuego','tituloJuego','textoJuego','precioJuego','fotoJuego','linkJuego','plataforma']
