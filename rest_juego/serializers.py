
from rest_framework import serializers
from PrayTheNews.models import Juego, Publicacion, Usuario

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['idJuego','tituloJuego','textoJuego','precioJuego'
                    ,'linkJuego','plataforma']

class JuegoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['idJuego','tituloJuego','textoJuego','precioJuego','fotoJuego','linkJuego','plataforma']



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario','nombreCompleto','correo','nickname','rol']





class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['idPublicacion','tituloPubli','descripcion','fechaP','usuario','tipo','status']

