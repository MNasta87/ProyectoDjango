
from django.urls import path
from .views import MenuNoticias, NoticiasIndividuales, NoticiaValorant



urlpatterns = [
    path('MenuNoticias/',MenuNoticias, name="MenuNoticias"),
    path('NoticiasIndividuales/',NoticiasIndividuales, name="NoticiasIndividuales"), 
    path('NoticiaValorant/',NoticiaValorant, name="NoticiaValorant"),   
]