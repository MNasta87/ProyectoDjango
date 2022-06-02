
from django.urls import path
from .views import CambiarContraAdmin, CuentaAdmin, CuentaPerio, EditarCuentaAdmin, EditarCuentaPerio, EditarCuentaU, FormularioUsuarios, GuardarCuentaAdmin, PerfilCompleto, PublicarAnalisis, RegistroAnalisis,RegistroNoticia,MenuNoticias, NoticiasIndividuales, NoticiaValorant,MenuPrincipal,Catalogo,MenuAnalisis,RegistroUsuarios,LoginUsuario,AdministrarUsuario,BuscarAnalisis,BuscarUsuario,EditarUsuario,CuentaUsuario,PerfilUsuario,PublicarNoticia 
                    



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
    #Admin
    path('PerfilAdmin/',CuentaAdmin,name="CuentaAdmin"),
    path('CambiarContraAdmin/',CambiarContraAdmin,name="CambiarContraAdmin"),
    
    path('EditarCuentaAdmin/',EditarCuentaAdmin,name="EditarCuentaAdmin"),
    path('GuardarCuentaAdmin/',GuardarCuentaAdmin,name="GuardarCuentaAdmin"),

    #Usuario
    path('Perfil/',PerfilUsuario,name="PerfilUsuario"),
    path('EditarCuenta/',EditarCuentaU,name="EditarCuentaU"),
    path('CuentaUsuario/',CuentaUsuario,name="CuentaUsuario"),
    #Periodista
    path('PerfilPeriodista/',CuentaPerio, name = "CuentaPerio"),
    path('EditarCuenta/',EditarCuentaPerio,name="EditarCuentaPerio"),

    #-
    path('Login/',LoginUsuario,name="LoginUsuario"), 
    path('AdministrarUsuario/',AdministrarUsuario,name="AdministrarUsuario"), 
    path('BuscarAnalisis/',BuscarAnalisis,name="BuscarAnalisis"),
    path('BuscarUsuario/',BuscarUsuario,name="BuscarUsuario"),
    path('EditarUsuario/',EditarUsuario,name="EditarUsuario"),
    
    
    
    path('PerfilRoman/<int:id>/',PerfilCompleto),




    #Paginas Normales
    path('NoticiasIndividuales/',NoticiasIndividuales, name="NoticiasIndividuales"), 
    path('NoticiaValorant/',NoticiaValorant, name="NoticiaValorant"),
    
    
]