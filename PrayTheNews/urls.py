
from django.urls import path 
from .views import CambiarContra, CuentaUsuario1, EditarCuenta, FormularioUsuarios, GuardarCambiarContra, GuardarCuenta,PerfilCompleto, PerfilConf, PublicarAnalisis, RegistroAnalisis,RegistroNoticia,MenuNoticias, NoticiasIndividuales, NoticiaValorant,MenuPrincipal,Catalogo,MenuAnalisis,RegistroUsuarios,LoginUsuario,AdministrarUsuario,BuscarPublicacion,BuscarUsuario,EditarUsuario,PublicarNoticia,Logout

from .views import CuentaAdmin, CuentaPerio,FormularioUsuarios, PerfilCompleto, PublicarAnalisis, RegistroAnalisis,RegistroNoticia,MenuNoticias, NoticiasIndividuales, NoticiaValorant,MenuPrincipal,Catalogo,MenuAnalisis,RegistroUsuarios,LoginUsuario,AdministrarUsuario,BuscarPublicacion,BuscarUsuario,EditarUsuario,PublicarNoticia 
                    




urlpatterns = [
    #Paginas Principales
    path('',MenuPrincipal,name="MenuPrincipal"),
    path('Noticias/',MenuNoticias,name="MenuNoticias"),
    path('Catalogo/',Catalogo,name="Catalogo"),
    path('Analisis/',MenuAnalisis,name="MenuAnalisis"),
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




    #Paginas Normales
    path('NoticiasIndividuales/',NoticiasIndividuales, name="NoticiasIndividuales"), 
    path('NoticiaValorant/',NoticiaValorant, name="NoticiaValorant"),
    
    
]