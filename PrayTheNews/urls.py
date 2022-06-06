
from django.urls import path 
from .views import AnalisisCompleto, AutorPerfil, BuscarUsuarios, CambiarContra, CuentaUsuario1, EditarCuenta, FormularioUsuarios, GuardarCambiarContra, GuardarCuenta, NoticiaCompleto,PerfilCompleto, PerfilConf, PublicarAnalisis, RegistroAnalisis,RegistroNoticia,Catalogo,RegistroUsuarios,LoginUsuario,AdministrarUsuario,BuscarPublicacion,BuscarUsuario,EditarUsuario,PublicarNoticia,Logout, index, indexMenuPrincipal, indexNoticia

from .views import CuentaAdmin, CuentaPerio,FormularioUsuarios, PerfilCompleto, PublicarAnalisis, RegistroAnalisis,RegistroNoticia,Catalogo,RegistroUsuarios,LoginUsuario,AdministrarUsuario,BuscarPublicacion,BuscarUsuario,EditarUsuario,PublicarNoticia 
                    




urlpatterns = [
    #Paginas Principales
    path('',indexMenuPrincipal,name="MenuPrincipal"),
    path('MenuNoticias/', indexNoticia,name="MenuNoticias"),
    path('Catalogo/',Catalogo,name="Catalogo"),
    path('MenuAnalisis/', index, name='MenuAnalisis'),
    

    #AUTOR

    path('Autor/<int:id>/',AutorPerfil), 

    #ANALISIS Y NOTICIAS INDIVIDUAL

    path('AnalisisTunic/<int:id>/',AnalisisCompleto),
    path('Noticia/<int:id>/',NoticiaCompleto),


    
    #P
    path('Formulario/',FormularioUsuarios,name="Formulario"),
    path('Registro/',RegistroUsuarios,name="RegistroUsuarios"),   

    path('PublicarNoticia/',PublicarNoticia,name="PublicarNoticia"),
    path('RegistroNoticia/',RegistroNoticia,name="RegistroNoticia"),

    path('PublicarAnalisis/',PublicarAnalisis,name="PublicarAnalisis"),
    path('RegistroAnalisis/',RegistroAnalisis,name="RegistroAnalisis"),

    #Perfiles
    path('EditarCuenta/',EditarCuenta,name="EditarCuenta"),
    path('GuardarCuenta/',GuardarCuenta,name="GuardarCuenta"),
    
    path('CambiarContra/',CambiarContra,name="CambiarContra"),
    path('GuardarCambiarContra/',GuardarCambiarContra,name="GuardarCambiarContra"),

    path('PerfilConf/',PerfilConf,name="PerfilConf"),
    
    #Buscar 
    path('BuscarUsuarios',BuscarUsuarios,name="BuscarUsuarios"),

    #Admin
    path('CuentaAdmin/',CuentaAdmin,name="CuentaAdmin"),

    #Usuario
    path('CuentaUsuario/',CuentaUsuario1,name="CuentaUsuario1"),
    #Periodista
    path('CuentaPeriodista/',CuentaPerio, name = "CuentaPerio"),
    

    #-
    path('Login/',LoginUsuario,name="LoginUsuario"), 
    path('Logout/',Logout,name="Logout"),
    path('AdministrarUsuario/',AdministrarUsuario,name="AdministrarUsuario"), 
    path('BuscarPublicacion/',BuscarPublicacion,name="BuscarPublicacion"),
    path('BuscarUsuario/',BuscarUsuario,name="BuscarUsuario"),
    path('EditarUsuario/',EditarUsuario,name="EditarUsuario"),
    
    
    
    path('PerfilRoman/<int:id>/',PerfilCompleto),

    
]