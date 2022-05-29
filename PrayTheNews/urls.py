
from django.urls import path
from .views import FormularioUsuarios,RegistroNoticia,MenuNoticias, NoticiasIndividuales, NoticiaValorant,MenuPrincipal,Catalogo,MenuAnalisis,RegistroUsuarios,LoginUsuario,AdministrarUsuario,BuscarAnalisis,BuscarUsuario,EditarUsuario,CuentaUsuario,EditarCuenta,PerfilUsuario,PublicarNoticia
                    



urlpatterns = [
    #Paginas Principales
    path('',MenuPrincipal,name="MenuPrincipal"),
    path('Noticias/',MenuNoticias,name="MenuNoticias"),
    path('Catalogo/',Catalogo,name="Catalogo"),
    path('Analisis/',MenuAnalisis,name="MenuAnalisis"),

    path('Formulario/',FormularioUsuarios,name="Formulario"),
    path('Registro/',RegistroUsuarios,name="RegistroUsuarios"),   

    path('PublicarNoticia/',PublicarNoticia,name="PublicarNoticia"),
    path('RegistroNoticia/',RegistroNoticia,name="RegistroNoticia"),


    path('Login/',LoginUsuario,name="LoginUsuario"), 
    path('AdministrarUsuario/',AdministrarUsuario,name="AdministrarUsuario"), 
    path('BuscarAnalisis/',BuscarAnalisis,name="BuscarAnalisis"),
    path('BuscarUsuario/',BuscarUsuario,name="BuscarUsuario"),
    path('EditarUsuario/',EditarUsuario,name="EditarUsuario"),
    path('CuentaUsuario/',CuentaUsuario,name="CuentaUsuario"),
    path('EditarCuenta/',EditarCuenta,name="EditarCuenta"),
    path('PerfilUsuario/',PerfilUsuario,name="PerfilUsuario"),
    




    #Paginas Normales
    path('NoticiasIndividuales/',NoticiasIndividuales, name="NoticiasIndividuales"), 
    path('NoticiaValorant/',NoticiaValorant, name="NoticiaValorant"),
    
    
]