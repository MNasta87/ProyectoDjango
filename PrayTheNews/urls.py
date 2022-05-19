from tokenize import Name
from unicodedata import name
from django.urls import path
from .views import MenuNoticias, NoticiasIndividuales



urlpatterns = [
    path('',MenuNoticias, name="MenuNoticias"),
    path('1',NoticiasIndividuales, name="NoticiasIndividuales"),    
]