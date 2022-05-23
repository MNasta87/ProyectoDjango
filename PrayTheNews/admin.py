from django.contrib import admin

from PrayTheNews.models import Juego, Rol,Usuario,Status,TipoPubli,Publicacion,Comentario,Parrafo

# Register your models here.

admin.site.register(Juego)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Status)
admin.site.register(TipoPubli)
admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(Parrafo)