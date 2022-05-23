from django.db import models

# Create your models here.

class Juego(models.Model):
    idJuego = models.AutoField(primary_key=True)
    tituloJuego = models.CharField(verbose_name='Titulo juego', max_length=50)
    textoJuego = models.CharField(max_length= 200,verbose_name= 'La descripcion')
    precioJuego = models.IntegerField(verbose_name='Precio del juego')
    fotoJuego = models.ImageField(upload_to="Juegos", null = False)
    linkJuego = models.CharField(max_length = 300, verbose_name='Link del juego')
    plataforma = models.CharField(max_length=20, verbose_name='Plataforma')

    def __str__(self):
        return self.tituloJuego