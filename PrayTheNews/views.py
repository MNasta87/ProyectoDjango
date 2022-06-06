import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime

from .models import Comentario, Parrafo, Publicacion, Status, TipoPubli, Usuario,Rol
# Create your views here.


def Catalogo(request):
    if 'usuario' in request.session:
        c_usuario = request.session['usuario']
        contexto = {'c_usuario': c_usuario}
        return render(request, 'PraytheNews/Catalogo/Catalogo.html', contexto)
    else:
        return render(request, 'PraytheNews/Catalogo/Catalogo.html')

def MenuAnalisis(request):
    if 'usuario' in request.session:
        c_usuario = request.session['usuario']
        contexto = {'c_usuario': c_usuario}
        return render(request, 'PraytheNews/Analisis/MenuAnalisis.html', contexto)
    else:
        return render(request, 'PraytheNews/Analisis/MenuAnalisis.html')

def FormularioUsuarios(request):
    return render(request,'PrayTheNews/Login/RegistroUsuario.html')






#Publicar Analisis
def PublicarAnalisis(request):
    return render(request, 'PrayTheNews/Analisis/PublicarAnalisis.html') 


def RegistroAnalisis(request):
    if request.method == "POST":

        PTitulo = request.POST['TituloPortada']
        PFoto = request.FILES['formFile']
        PDescripcion = request.POST['DPortada']
        fechaActual = datetime.today().strftime('%Y-%m-%d')

        T_Parrafo1 = request.POST['TParrafo1']
        F_Parrafo1 = request.FILES['FParrafo1']
        D_Parrafo1 = request.POST['DParrafo1']

        T_Parrafo2 = request.POST['TParrafo2']
        F_Parrafo2 = request.FILES['FParrafo2']
        D_Parrafo2 = request.POST['DParrafo2']

        T_Parrafo3 = request.POST['TParrafo3']
        F_Parrafo3 = request.FILES['FParrafo3']
        D_Parrafo3 = request.POST['DParrafo3']

        Conclusion = request.POST['Conclusion']

        c_usuario = request.session['usuario']

        U_usuario = Usuario.objects.get(nickname = c_usuario)
        T_tipo = TipoPubli.objects.get(idTipo = 3)# 2 es tipo conclusion
        S_status = Status.objects.get(idStatus = 1)

        

        if (PTitulo != '' or PFoto != '' or PDescripcion != '' or T_Parrafo1 != '' or F_Parrafo1 != '' or D_Parrafo1 != '' or Conclusion != ''
            or T_Parrafo2 != '' or F_Parrafo2 != '' or D_Parrafo2 != ''or T_Parrafo3 != '' or F_Parrafo3 != '' or D_Parrafo3 != ''):
            
            Publicacion.objects.create(fotoPortada = PFoto, tituloPubli = PTitulo, descripcion = PDescripcion, 
                                        fechaP = fechaActual , conclusionP = Conclusion , usuario = U_usuario ,tipo = T_tipo , status = S_status)
            
            Parrafo.objects.create( tituloParrafo = T_Parrafo1 ,fotoParrafo =  F_Parrafo1, descripcion = D_Parrafo1 , idPublicacion = Publicacion.objects.get(descripcion = PDescripcion))
            
            Parrafo.objects.create( tituloParrafo = T_Parrafo2 ,fotoParrafo=  F_Parrafo2, descripcion = D_Parrafo2 , idPublicacion = Publicacion.objects.get(descripcion = PDescripcion))

            Parrafo.objects.create( tituloParrafo = T_Parrafo3 ,fotoParrafo=  F_Parrafo3, descripcion = D_Parrafo3 , idPublicacion = Publicacion.objects.get(descripcion = PDescripcion))

            messages.success(request,'Analisis registrado!')
            
            return redirect('PublicarAnalisis')                 

        else:
            messages.error(request,"Rellena el formulario")
            return redirect('PublicarAnalisis')

    else:
        print("---------------------------Error en el POST-------------------")
        return redirect('PublicarAnalisis')
    
#Publicar noticia
def PublicarNoticia(request):
    return render(request, 'PrayTheNews/Noticias/PublicarNoticia.html')

def RegistroNoticia(request):

    if request.method == "POST":

        PTitulo = request.POST['TituloPortada']
        PFoto = request.FILES['formFile']
        PDescripcion = request.POST['DPortada']
        fechaActual = datetime.today().strftime('%Y-%m-%d')

        T_Parrafo1 = request.POST['TParrafo1']
        F_Parrafo1 = request.FILES['FParrafo1']
        D_Parrafo1 = request.POST['DParrafo1']

        T_Parrafo2 = request.POST['TParrafo2']
        F_Parrafo2 = request.FILES['FParrafo2']
        D_Parrafo2 = request.POST['DParrafo2']

        T_Parrafo3 = request.POST['TParrafo3']
        F_Parrafo3 = request.FILES['FParrafo3']
        D_Parrafo3 = request.POST['DParrafo3']

        c_usuario = request.session['usuario']

        U_usuario = Usuario.objects.get(nickname = c_usuario)
        T_tipo = TipoPubli.objects.get(idTipo = 4)
        S_status = Status.objects.get(idStatus = 1)

        

        if (PTitulo != '' or PFoto != '' or PDescripcion != '' or T_Parrafo1 != '' or F_Parrafo1 != '' or D_Parrafo1 != '' 
            or T_Parrafo2 != '' or F_Parrafo2 != '' or D_Parrafo2 != ''or T_Parrafo3 != '' or F_Parrafo3 != '' or D_Parrafo3 != ''):
            
            Publicacion.objects.create(fotoPortada = PFoto, tituloPubli = PTitulo, descripcion = PDescripcion, 
                                        fechaP = fechaActual , usuario = U_usuario ,tipo = T_tipo , status = S_status)

            
            Parrafo.objects.create( tituloParrafo = T_Parrafo1 ,fotoParrafo =  F_Parrafo1, descripcion = D_Parrafo1 , idPublicacion = Publicacion.objects.get(descripcion = PDescripcion))

            Parrafo.objects.create( tituloParrafo = T_Parrafo2 ,fotoParrafo=  F_Parrafo2, descripcion = D_Parrafo2 , idPublicacion = Publicacion.objects.get(descripcion = PDescripcion))

            Parrafo.objects.create( tituloParrafo = T_Parrafo3 ,fotoParrafo=  F_Parrafo3, descripcion = D_Parrafo3 , idPublicacion = Publicacion.objects.get(descripcion = PDescripcion))

            messages.success(request,'Noticia Registrada!')
            
            return redirect('PublicarNoticia')                 

        else:
            messages.error(request,"Rellena el formulario")
            return redirect('PublicarNoticia')

    else:
        print("---------------------------Error en el POST-------------------")
        return redirect('PublicarNoticia')
#------------------Cuentas-----------

def PerfilConf(request):
    c_usuario = request.session['usuario']
    try:
        U_usuario = Usuario.objects.get(nickname = c_usuario)
    except Usuario.DoesNotExist:
        U_usuario = None

    try:
        Admin = Usuario.objects.get(nickname = c_usuario,rol = 3)#"Administrador"
    except Usuario.DoesNotExist:
        Admin = None

    try:
        Usu = Usuario.objects.get(nickname = c_usuario,rol = 1 )#"Usuario"
    except Usuario.DoesNotExist:
        Usu = None

    try:
        Perio = Usuario.objects.get(nickname = c_usuario,rol = 2)#"Periodista"
    except Usuario.DoesNotExist:
        Perio = None

    
    if(U_usuario is not None):

        if(Admin is not None):
            print("------------------------------Admin--------------------------------")
            return redirect('CuentaAdmin')

        if(Perio is not None):
            print("------------------------------Perio--------------------------------")
            return redirect('CuentaPerio')

        if(Usu is not None):
            print("------------------------------Usu--------------------------------")
            return redirect('CuentaUsuario1')
            
        else:
            print("--------------------------------------------------------------")
            print("------------ERROR EN EL USUARIO---------")
            return redirect('MenuPrincipal')  
    
    else:
        print("--------------------------------------------------------------")
        print("------------ERROR EN EL USUARIO 11---------")
        return redirect('MenuPrincipal')   


def EditarCuenta(request):
    Nick = request.session['usuario']
    try:
        InfoUsuario = Usuario.objects.get(nickname = Nick)
    except Usuario.DoesNotExist:
        InfoUsuario = None
    
    
    contexto = {'nombreCompleto': InfoUsuario.nombreCompleto,'correo': InfoUsuario.correo,'nickname': InfoUsuario.nickname,'fotoUsuario': InfoUsuario.fotoUsuario,
    'linkInstagram': InfoUsuario.linkInstagram,'linkTwitch': InfoUsuario.linkTwitch,'linkTwitter': InfoUsuario.linkTwitter,'rol': InfoUsuario.rol}
    return render(request,'PrayTheNews/Usuario/EditarCuenta.html', contexto)

def GuardarCuenta(request):

    if request.method == "POST":

        NickName = request.POST['Nick']
        Foto = request.FILES.get('FotoU','')
        Correo = request.POST['Correo']
        Nombres = request.POST['Nombres']
        contra = request.POST['Contra']

        Redtwitch = request.POST['Redtwitch']
        RedInsta = request.POST['RedInsta']
        RedTwitter = request.POST['RedTwitter']
        

        try:
            Perfil = Usuario.objects.get( clave = contra,correo = Correo)
        except Usuario.DoesNotExist:
            Perfil = None
            #Comprobar si Cambio su propio nick 
        try: 
            CambioNick = Usuario.objects.get( nickname = NickName , correo = Correo)
        except Usuario.DoesNotExist:
            CambioNick  = None

        try: 
            ExisteNick = Usuario.objects.get(nickname = NickName)
        except Usuario.DoesNotExist:
            ExisteNick  = None 

        NoGuardo = ""

        if Perfil is not None:

            if CambioNick is None:
                if ExisteNick is None:
                    Perfil.nickname = NickName
                else:
                    NoGuardo = " Menos el nick. Ya existe"
                    
            if Foto != '':
                Perfil.fotoUsuario = Foto
            
            if RedInsta != '':
                Perfil.linkInstagram = RedInsta

            if Redtwitch != '':
                Perfil.linkTwitch = Redtwitch

            if RedTwitter != '':
                Perfil.linkTwitter = RedTwitter
            
            if Nombres != '': 
                Perfil.nombreCompleto = Nombres
                        
            Perfil.save()            
            messages.success(request, "Se Guardaron los datos."+ NoGuardo)            
            return redirect('EditarCuenta')             

        else:
            messages.error(request, "La Contraseña es incorrecta.")
            return redirect('EditarCuenta')

    else:
        print("---------------------------Error en el POST-------------------")
        return redirect('EditarCuenta')

def CambiarContra(request):
    return render(request,'PrayTheNews/Usuario/CambiarContra.html')

def GuardarCambiarContra(request):

    if request.method == "POST":

        c_usuario = request.session['usuario']

        U_usuario = Usuario.objects.get(nickname = c_usuario)
        Correo = U_usuario.correo

        ContraActual = request.POST['contra']
        Contra1 = request.POST['contra2']
        Contra2 = request.POST['contra3']

        try:
            Perfil = Usuario.objects.get( clave = ContraActual ,correo = Correo)
        except Usuario.DoesNotExist:
            Perfil = None

    
        if(Perfil is not None):
            if(Contra1 == Contra2):
                Perfil.clave = Contra1
                Perfil.save()     
                messages.success(request, "La contraseña a sido modificada")            
                return redirect('CambiarContra')

            else:
                messages.success(request, "Las contraseñas nuevas no son iguales.")            
                return redirect('CambiarContra')
        else:
            messages.success(request, "La contraseña Actual es incorrecta.")            
            return redirect('CambiarContra')
    else:
        print("---------------------------Error en el POST-------------------")
        return redirect('CambiarContra')
    
#Periodista
def CuentaPerio(request):
    Nick = request.session['usuario']
    try:
        InfoUsuario = Usuario.objects.get(nickname = Nick)
    except Usuario.DoesNotExist:
        InfoUsuario = None

    contexto = {'nombreCompleto': InfoUsuario.nombreCompleto,'correo': InfoUsuario.correo,'nickname': InfoUsuario.nickname,'fotoUsuario': InfoUsuario.fotoUsuario,
    'linkInstagram': InfoUsuario.linkInstagram,'linkTwitch': InfoUsuario.linkTwitch,'linkTwitter': InfoUsuario.linkTwitter,'rol': InfoUsuario.rol}

    return render(request,'PrayTheNews/Periodista/CuentaPeriodista.html', contexto)

#Usuario Normal 
def CuentaUsuario1(request):
    Nick = request.session['usuario']
    try:
        InfoUsuario = Usuario.objects.get(nickname = Nick)
    except Usuario.DoesNotExist:
        InfoUsuario = None

    contexto = {'nombreCompleto': InfoUsuario.nombreCompleto,'correo': InfoUsuario.correo,'nickname': InfoUsuario.nickname,'fotoUsuario': InfoUsuario.fotoUsuario,
    'linkInstagram': InfoUsuario.linkInstagram,'linkTwitch': InfoUsuario.linkTwitch,'linkTwitter': InfoUsuario.linkTwitter,'rol': InfoUsuario.rol}

    return render(request,'PrayTheNews/Usuario/CuentaUsuario.html', contexto)

#Cosas de Admin------------------------------
#Cuenta Admin 
def CuentaAdmin(request):
    Nick = request.session['usuario']
    try:
        InfoUsuario = Usuario.objects.get(nickname = Nick)
    except Usuario.DoesNotExist:
        InfoUsuario = None

    contexto = {'nombreCompleto': InfoUsuario.nombreCompleto,'correo': InfoUsuario.correo,'nickname': InfoUsuario.nickname,'fotoUsuario': InfoUsuario.fotoUsuario,
    'linkInstagram': InfoUsuario.linkInstagram,'linkTwitch': InfoUsuario.linkTwitch,'linkTwitter': InfoUsuario.linkTwitter,'rol': InfoUsuario.rol}

    return render(request,'PrayTheNews/Admin/CuentaAdmin.html', contexto)

#Buscar Analisis
def BuscarAnalisis(request):
    lista_Analisis = Publicacion.objects.filter(tipo='3')

    contexto ={"lista_Publicacion" : lista_Analisis}
    return render(request, 'PraytheNews/Buscar/BuscarAnalisis.html',contexto) 


def BuscarNoticia(request):
    lista_Noticia = Publicacion.objects.filter(tipo='4')

    contexto ={"lista_Publicacion" : lista_Noticia}
    return render(request, 'PraytheNews/Buscar/BuscarNoticias.html',contexto) 

def eliminar_Analisis(request, id):
    publi = Publicacion.objects.get(idPublicacion = id)
    publi.delete() #elimina el registro
    messages.success(request,'Publicacion Eliminada')
    return redirect('BuscarAnalisis')

def eliminar_Noticias(request, id):
    publi = Publicacion.objects.get(idPublicacion = id)
    publi.delete() #elimina el registro
    messages.success(request,'Publicacion Eliminada')
    return redirect('BuscarNoticia')   

def Visualizar_Publicacion():
    return redirect('BuscarAnalisis')



##def BuscarNoticia(request): codigo original del matias
    #lista_Publicacion = Publicacion.objects.all()
    #tipo_publicacion = request.GET.get('tipo_publicacion')
    #if  is_valid_queryparam(tipo_publicacion):
        #lista_Publicacion = lista_Publicacion.filter(tipo = tipo_publicacion)
        #return render(request, 'PraytheNews/Admin/BuscarPublicacion.html',{'lista_Publicacion': lista_Publicacion})
    ##else: 
        #return render(request, 'PraytheNews/Admin/BuscarPublicacion.html', {'lista_Publicacion': lista_Publicacion})

#Eliminar Usuarios
def eliminar_Usuario (request, id):
    usuario = Usuario.objects.get(idUsuario = id)
    
    usuario.delete() #elimina el registro
    messages.success(request,'Usuario Eliminado')

    return redirect('BuscarUsuarios')
    
#BuscarUsuarios
def BuscarUsuarios(request):
    Usuarios = Usuario.objects.all()
    contexto ={"Usuarios" : Usuarios}
    return render(request, 'PrayTheNews/Buscar/BuscarUsuarios.html',contexto ) 


#Modificar Usuarios
def modificar_Usuario(request, id):
    InfoUsuario = Usuario.objects.get(idUsuario = id)
    Roles = Rol.objects.all() #obtener todas los roles para llenar el combobox

    contexto = {
        'nombreCompleto': InfoUsuario.nombreCompleto,'correo': InfoUsuario.correo,'nickname': InfoUsuario.nickname,'fotoUsuario': InfoUsuario.fotoUsuario,
        'linkInstagram': InfoUsuario.linkInstagram,'linkTwitch': InfoUsuario.linkTwitch,'linkTwitter': InfoUsuario.linkTwitter,'rol': InfoUsuario.rol,
        "Roles" : Roles
    }

    return render(request,'PrayTheNews/Buscar/EditarCuentasUsuarios.html',contexto)

# Guardar la Modificacion de Usuarios
def GuardarCuentaUsuarios(request):

    if request.method == "POST":

        NickName = request.POST['Nick']
        Foto = request.FILES.get('FotoU','')
        Correo = request.POST['Correo']
        Nombres = request.POST['Nombres']
        rol = request.POST['rol']
        

        Redtwitch = request.POST['Redtwitch']
        RedInsta = request.POST['RedInsta']
        RedTwitter = request.POST['RedTwitter']
        

        try:
            Perfil = Usuario.objects.get(correo = Correo)
        except Usuario.DoesNotExist:
            Perfil = None
            #Comprobar si Cambio su propio nick 
        try: 
            CambioNick = Usuario.objects.get( nickname = NickName , correo = Correo)
        except Usuario.DoesNotExist:
            CambioNick  = None

        try: 
            ExisteNick = Usuario.objects.get(nickname = NickName)
        except Usuario.DoesNotExist:
            ExisteNick  = None 

        NoGuardo = ""

        rol1 = Rol.objects.get(idRol = rol)

        Perfil.rol = rol1

        if CambioNick is None:
            if ExisteNick is None:
                Perfil.nickname = NickName
            else:
                NoGuardo = " Menos el nick. Ya existe"
                    
        if Foto != '':
            Perfil.fotoUsuario = Foto
            
        if RedInsta != '':
            Perfil.linkInstagram = RedInsta

        if Redtwitch != '':
            Perfil.linkTwitch = Redtwitch

        if RedTwitter != '':
            Perfil.linkTwitter = RedTwitter
            
        if Nombres != '': 
            Perfil.nombreCompleto = Nombres
                        
        Perfil.save()            
        messages.success(request, "Se Guardaron los datos."+ NoGuardo)            
        return redirect('modificar_Usuario',Perfil.idUsuario)             

    else:
        print("---------------------------Error en el POST-------------------")
        return redirect('modificar_Usuario',Perfil.idUsuario)


#--------Fin Cosas de Admin------------------------------
    
#----------------Fin Cuentas-----------    

# Registro nuevo Usuario
def RegistroUsuarios(request):
    # aqui no va el if del post porque daba errores
    nombreCompleto_U = request.POST.get('nombre', False)
    correo_U = request.POST.get('correo', False)
    clave_U = request.POST.get('password', False)
    clave2 = request.POST.get('password2',False)
    nickname_U = request.POST.get('usuario', False)

    linkInstagram_U = ''
    linkTwitch_U = ''
    linkTwitter_U = ''

    rol_u = Rol.objects.get(idRol = 1)
    #1 de rol de usuario
    
    try:
        nombre = Usuario.objects.get( nickname = nickname_U)
    except Usuario.DoesNotExist:
        nombre = None
    try:
        corr = Usuario.objects.get( correo = correo_U)
    except Usuario.DoesNotExist:
        corr = None


    if clave2 != False:
        if clave_U == clave2:
            if nombre is None:
                if corr is None:
                    Usuario.objects.create(nombreCompleto = nombreCompleto_U, correo = correo_U,clave = clave_U,
                    nickname = nickname_U,linkInstagram = linkInstagram_U, linkTwitch = linkTwitch_U,
                    linkTwitter= linkTwitter_U, rol = rol_u)
                    
                    return redirect('LoginUsuario')
                else:
                    messages.error(request, "El correo ya esta vinculado a una cuenta")
                    return redirect('Formulario')
            else:
                messages.error(request, "El NickName ya existe")
                return redirect('Formulario')
        else:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('Formulario') 
    else:
        print("--------------------------------------------------")
        print(clave2)
        return redirect('Formulario') 

def LoginUsuario(request):
    if request.method == 'POST':
        Correo = request.POST.get('Correo')
        clave = request.POST.get('clave')
        try:
            usuario = Usuario.objects.get(correo=Correo, clave=clave)
        except Usuario.DoesNotExist:
            usuario = None
        if usuario:
            nick = usuario.nickname
            request.session['usuario']= nick
            return redirect('MenuPrincipal')
        else:
            messages.info(request, "El correo o Contraseña Son Incorrectos")
            return redirect('LoginUsuario')

    else:
        return render(request, 'PrayTheNews/Login/LoginUsuario.html')
	

def Logout(request):
    try:
        del request.session['usuario']
    except:
        return redirect('LoginUsuario')
    return redirect('LoginUsuario')	

def is_valid_queryparam(param):
    return param != '' and param is not None

def AdministrarUsuario(request):
    return render(request, 'PrayTheNews/Admin/AdministrarUsuario.html')


def BuscarUsuario(request):
    lista_usuario = Usuario.objects.all()
    rol_usuario = request.GET.get('tipo_usuario')

    if is_valid_queryparam(rol_usuario):
        lista_usuario = lista_usuario.filter(rol = rol_usuario)
        return render(request, 'PraytheNews/Admin/BuscarUsuarios.html', {'lista_usuario': lista_usuario})
    else:
        return render(request, 'PraytheNews/Admin/BuscarUsuarios.html', {'lista_usuario': lista_usuario})
    

def EditarUsuario(request):
    return render(request, 'PrayTheNews/Admin/EditarUsuarios.html')

def PerfilCompleto(request, id):

    Profile = Usuario.objects.get(idUsuario=id)
    
    contexto2 = {

        "perfil": Profile


    }

    return render(request, "PrayTheNews/Usuario/PerfilRoman.html", contexto2)



# MENU ANALISIS, PLANTILLA ANALISIS



def index(request): #Analisis
    articles = Publicacion.objects.filter(status='1',tipo='3').order_by('-fechaP')
    articlesP = Publicacion.objects.filter(status='1',tipo='3').order_by('fechaP')
    
    

    # Pagination
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

    paginator = Paginator(articlesP, 1)
    page_number = request.GET.get('page')
    articles_paginatorP = paginator.get_page(page_number)

    template = loader.get_template('PrayTheNews/Analisis/indexMenuAnalisis.html')

    context = {
        'articles': articles_paginator,
        'articuloP': articles_paginatorP,
        

    }

    

    if 'usuario' in request.session:
        c_usuario = request.session['usuario']
        context = {
        'articles': articles_paginator,
        'articuloP': articles_paginatorP,
        'c_usuario': c_usuario,

    }
        return HttpResponse(template.render(context, request))

    else:
        context = {
        'articles': articles_paginator,
        'articuloP': articles_paginatorP,
    }
        return HttpResponse(template.render(context, request))




# ANALISIS INDIVIDUAL


def AnalisisCompleto(request, id):

    analisis = Publicacion.objects.get(idPublicacion=id)
    parrafos = Parrafo.objects.filter(idPublicacion=analisis)
    

    contexto2 = {

        'analis': analisis,
        'P1': parrafos,



    }

    return render(request, "PrayTheNews/Analisis/individual/indexAnalisis.html", contexto2)


# PERFIL AUTOR



def AutorPerfil(request, id):

    user = Usuario.objects.get(idUsuario=id)
    articles = Publicacion.objects.filter(usuario=user)
    countA = Publicacion.objects.filter(usuario=user, tipo='4').count()
    countN = Publicacion.objects.filter(usuario=user, tipo='3').count()
    

    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)



    return render(request, 'PrayTheNews/Autor/PerfilAutor.html', {'us': user,'articlesA': articles_paginator, 'count': countA,'countN':countN})


# MENU PRINCIPAL


def indexMenuPrincipal(request): 
    articles1 = Publicacion.objects.filter(status='1',tipo='3').order_by('-fechaP')

    
    articles2 = Publicacion.objects.filter(status='1',tipo='4').order_by('-fechaP')

    articles3 = Publicacion.objects.filter(status='1',tipo='4').order_by('fechaP')
    
    

    # Pagination
    paginator = Paginator(articles1, 3)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

    paginator = Paginator(articles2, 2)
    page_number = request.GET.get('page')
    articles_paginatorP = paginator.get_page(page_number)

    paginator = Paginator(articles3, 1)
    page_number = request.GET.get('page')
    articles_paginatorP1 = paginator.get_page(page_number)

    template = loader.get_template('PrayTheNews/MenuPrincipal/indexMenu.html')

    if 'usuario' in request.session:
        c_usuario = request.session['usuario']
        context = {
        'articlesM': articles_paginator,
        'articuloMP': articles_paginatorP,
        'articuloP1': articles_paginatorP1,
        'c_usuario': c_usuario,

    }
        return HttpResponse(template.render(context, request))

    else:
        context = {
        'articlesM': articles_paginator,
        'articuloMP': articles_paginatorP,
        'articuloP1': articles_paginatorP1,
    }
        return HttpResponse(template.render(context, request))

    




# MENU NOTICIAS 

def indexNoticia(request): 
    articles = Publicacion.objects.filter(status='1',tipo='4').order_by('-fechaP')
    articlesP = Publicacion.objects.filter(status='1',tipo='4').order_by('fechaP')
    
    

    # Pagination
    paginator = Paginator(articles, 1)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

    paginator = Paginator(articlesP, 1)
    page_number = request.GET.get('page')
    articles_paginatorP = paginator.get_page(page_number)

    template = loader.get_template('PrayTheNews/NoticiasListo/indexMenuNoticia.html')

    if 'usuario' in request.session:
        c_usuario = request.session['usuario']
        context = {
        'noticia': articles_paginator,
        'noticiaP': articles_paginatorP,
        'c_usuario': c_usuario,
        
    }
        return HttpResponse(template.render(context, request))

    else:
        context = {
        'noticia': articles_paginator,
        'noticiaP': articles_paginatorP,
        
    }
        return HttpResponse(template.render(context, request))

    
#Comentarios
def publicarComentario(request):

    
    if request.method == "POST":

        nick = request.POST['nick']
        comen = request.POST['comentario']
        idPubli = request.POST['idPubli']
        fechaComentario = datetime.today().strftime('%Y-%m-%d')

        publi = Publicacion.objects.get(idPublicacion = idPubli)
        S_status = Status.objects.get(idStatus = 1)
        
        try:
            nombre = Usuario.objects.get( nickname = nick)
        except Usuario.DoesNotExist:
            nombre = None
        
        if (nick != '' and comen != '' and nombre is not None):

            Comentario.objects.create(descripcion = comen, fechaComentario = fechaComentario, status = S_status, 
                                        usuario = nombre , idPublicacion = publi)

            return redirect('NoticiaCompleto',idPubli)

        else:
            print("Error en el usaurio----------")
            return redirect('NoticiaCompleto',idPubli)

    else:
        print(" Error en el póst---------------------------")
        return redirect('NoticiaCompleto',idPubli)

# NOTICIAS INDIVIDUAL


def NoticiaCompleto(request, id):
    
    noticias = Publicacion.objects.get(idPublicacion=id, tipo='4')
    parrafos = Parrafo.objects.filter(idPublicacion=noticias)

    c_usuario = request.session['usuario']

    contexto2 = {

        'noticia': noticias,
        'P2': parrafos,
        'nick': c_usuario,
        'c_usuario': c_usuario,
  
    }

    return render(request, "PrayTheNews/NoticiasListo/Individual/indexNoticia.html", contexto2)


def NoticiaCompleto2(request, id): 

    noticias = Publicacion.objects.get(idPublicacion=id, tipo='4')
    parrafos = Parrafo.objects.filter(idPublicacion=noticias)
    comentario = Comentario.objects.filter(idPublicacion=noticias)
    

    # Pagination
    paginator = Paginator(comentario, 3)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

    c_usuario = request.session['usuario']
    idPubli = noticias.idPublicacion


    template = loader.get_template('PrayTheNews/NoticiasListo/Individual/indexNoticia.html')

    context = {
        'noticia': noticias,
        'P2': parrafos,
        'comentario': articles_paginator,
        'id_Publi' : idPubli,
        'c_usuario': c_usuario

    }

    return HttpResponse(template.render(context, request))