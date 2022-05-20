
from django.urls import path
from .views import MenuNoticias, NoticiasIndividuales, NoticiaValorant,MenuPrincipal,Catalogo



urlpatterns = [
    #Paginas Principales
    path('',MenuPrincipal,name="MenuPrincipal"),
    path('MenuNoticias/',MenuNoticias, name="MenuNoticias"),
    path('Catalogo/',Catalogo,name="Catalogo"),   



    #Paginas Normales
    path('NoticiasIndividuales/',NoticiasIndividuales, name="NoticiasIndividuales"), 
    path('NoticiaValorant/',NoticiaValorant, name="NoticiaValorant"),
    
    
]