from django.db import models

# Create your models here.

# Tabla sola juegos
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


# Creacion usuario

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True,verbose_name="Código de rol")
    nombre = models.CharField(max_length=30, verbose_name="Nombre del tipo de usuario",null=False, blank=False)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True,verbose_name="Id del usuario")
    nombreCompleto = models.CharField(max_length=40, verbose_name="Nombre del usuario",null=False, blank=False)
    correo = models.EmailField(max_length=40, verbose_name="Correo Electronico",null=False, blank=False)
    clave = models.CharField(max_length=200, verbose_name="Contrasenna",null=False, blank=False)
    nickname = models.CharField(max_length=15, verbose_name="NickName",null=False, blank=False)
    fotoUsuario = models.ImageField(default='users/user_default_profile.png',upload_to="FotosUsuarios")
    telefono = models.CharField(max_length=50,null=True, blank=True)
    linkInstagram = models.CharField(max_length=100, verbose_name="Redes sociales intagram", blank=True)
    linkTwitch = models.CharField(max_length=100, verbose_name="Redes sociales twitch", blank=True)
    linkTwitter = models.CharField(max_length=100, verbose_name="Redes sociales twitter", blank=True)
    rol = models.ForeignKey(Rol,on_delete= models.CASCADE)


    def __str__(self):
        return self.nombreCompleto
        




# creacion de sub tablas de publicacion

class Status(models.Model):
    idStatus = models.AutoField(primary_key=True,verbose_name="Status de comentario/publicacion *baneo")
    nombres = models.CharField(max_length=100, verbose_name="Nombre del Status",null=False, blank=False)

    def __str__(self):
        return self.nombres



class TipoPubli(models.Model):
    idTipo = models.AutoField(primary_key=True,verbose_name="codigo del tipo de la publicacion")
    nombreTipo= models.CharField(max_length=30, verbose_name="Tipo de publicacion",null=False, blank=False)

    def __str__(self):
        return self.nombreTipo


# Creacion de publicacion main

class Publicacion(models.Model):
    idPublicacion = models.AutoField(primary_key=True,verbose_name="Código de la publicacion")
    fotoPortada = models.ImageField(upload_to="Foto_Portada",null=False, blank=False )
    tituloPubli = models.CharField(max_length=200, verbose_name="Titulo de la publicacion",null=False, blank=False)
    descripcion = models.CharField(max_length=1000, verbose_name="Descripcion de la publicacion",null=False, blank=False)
    fechaP = models.DateField(verbose_name="Fecha de la publicacion",null=False, blank=False)
    conclusionP = models.CharField(max_length=900, verbose_name="Conclusion Opcional", blank=True)


    usuario = models.ForeignKey(Usuario,on_delete= models.CASCADE,verbose_name="Autor de la publicacion",null=False, blank=False)
    tipo = models.ForeignKey(TipoPubli,on_delete= models.CASCADE, verbose_name="Tipo de publicacion",null=False, blank=False)
    status = models.ForeignKey(Status,on_delete= models.CASCADE,verbose_name="Baneo",null=False, blank=False)


    def __str__(self):
        return self.tituloPubli

# Creacion de Sector de comentarios

class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True, verbose_name="id comentario")
    descripcion = models.TextField(max_length=550, verbose_name="Contenido de comentario")
    fechaComentario = models.DateField(null=False)


    status = models.ForeignKey(Status,on_delete= models.CASCADE, verbose_name="Baneo")
    usuario = models.ForeignKey(Usuario,on_delete= models.CASCADE,verbose_name="Usuario que comento")
    idPublicacion = models.ForeignKey(Publicacion,on_delete= models.CASCADE,verbose_name= "Id publicacion")

    def __str__(self):
        return self.fechaComentario

# Parrafos de la Publicacion

class Parrafo(models.Model):
    idParrafo = models.AutoField(primary_key=True,verbose_name="Código del parrafo")
    tituloParrafo = models.CharField(max_length=200, verbose_name="Titulo del parrafo", blank=False)
    descripcion = models.TextField(max_length=2000, verbose_name="Descripcion del parrafo",null= False,blank=True)
    fotoParrafo = models.ImageField(upload_to="Foto_del_parrafo")
    idPublicacion = models.ForeignKey(Publicacion,on_delete= models.CASCADE)


    def __str__(self):
        return self.tituloParrafo



