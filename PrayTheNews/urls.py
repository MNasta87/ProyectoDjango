
from django.urls import path
from .views import MenuNoticias, NoticiasIndividuales, NoticiaValorant,MenuPrincipal,Catalogo,MenuAnalisis



urlpatterns = [
    #Paginas Principales
    path('',MenuPrincipal,name="MenuPrincipal"),
    path('Noticias/',MenuNoticias, name="MenuNoticias"),
    path('Catalogo/',Catalogo,name="Catalogo"),
    path('MenuAnalisis/',MenuAnalisis,name="MenuAnalisis"),   



    #Paginas Normales
    path('NoticiasIndividuales/',NoticiasIndividuales, name="NoticiasIndividuales"), 
    path('NoticiaValorant/',NoticiaValorant, name="NoticiaValorant"),
    
    
]