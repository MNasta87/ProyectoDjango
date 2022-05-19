from django.shortcuts import render

# Create your views here.
def MenuNoticias(request):
    Noticia ={"titulo1":" La solución de Riot a los problemas en el Deathmatch de Valorant", 
                "contenido1":"  Hace unos días Riot Games lanzó de manera oficial el Parche 4.03 de Valorant, y con él una nueva serie de ajustes a Agentes, modos de juego y errores que van surgiendo actualización tras actualización. La salida de este nuevo parche trajo consigo una nueva problemática, esta vez en el modo de juego Deathmatch.", 
                "miniatura1":"/static/PrayTheNews/img_noticia/img/Valorant-Two-German-leagues-coming-next-year.jpg",

            "titulo2":"Joven Muy triste por la salida videojuego POU de la Google Store",
               "contenido2":" Así lo había declarado el 2 de diciembre, Paul Salameh, el creador de Pou, quien anunció que el juego sería descontinuado de la tienda de Android (Google Play) sin dar motivos aparentes de la eliminación.",
               "miniatura2":"/static/PrayTheNews/img_noticia/img/Pou-Foto-Archivo.jpg" ,
            "titulo3":"El Nuevo videojuego basado en la saga Harry Potter",
                "contenido3":" El Videojuego de la saga de harry potter asombra a todos con nuevo trailer mostrando las caracteristicas que va a tener el videojuego, Hogwarts Legacy es un RPG de acción inmersivo en mundo abierto que se inspira de los libros de la saga Harry Potter a cargo de Avalanche Software y Warner Bros. Tu personaje es un alumno o alumna del famoso colegio que tiene la clave de un antiguo secreto que amenaza con destruir el mundo mágico.",
                "miniatura3":"/static/PrayTheNews/img_noticia/img/hogwarts-legacy-1-1601466696.jpg",
            "titulo4":"Elden Ring: uno de los mejores juegos de la historia",
                "contenido4":"Desde el lanzamiento de Elden Ring el pasado 25 de febrero hemos visto cómo ha arrasado en la listas de ventas físicas y digitales de distintos  países.",
                "miniatura4":"static/PrayTheNews/img_noticia/img/gm-d9aca072-2f2d-49a5-ae25-0e2504921135-elden-ring-4k-screenshot.jpg",
            "titulo5":"Horizon Forbidden West no gusta a los japoneses y vende menos que el anterior",
                "contenido5":"Las ventas conseguidas por Horizon Forbidden West en cada país no son muy alentadoras. Y es que lo último de Guerrilla se ha colocado como el segundo mayor lanzamiento de PS5 en el mercado británico mientras que los resultados desde Japón nos gritan que Horizon Forbidden West es un fracaso, al menos en las primeras estimaciones de venta de sus copias físicas.",
                "miniatura5":"static/PrayTheNews/img_noticia/img/horizon-forbidden-west-ps5-playstation-5-1.webp"}
                              
    
    return render(request, 'PrayTheNews/MenuNoticias.html', Noticia)

def NoticiasIndividuales(request):

    Titulos={"titulo":"Hollow Knight SilkSong", 
                "encabezado":"Hollow Knight Silksong: El juego que todos esperan pero del que no se sabe nada",
                "subtitulo1":"Con 5 años desde la salida hollow knight cautivó a muchos jugadores, no obstante, no se sabe mucho sobre su esperada secuela.",
                "subtitulo2":"¿CUÁNDO ES LA FECHA DE LANZAMIENTO DE HOLLOW KNIGHT SILKSONG?",
                "subtitulo3":"¿VIENE HOLLOW KNIGHT SILKSONG A SWITCH?",
                "subtitulo4":"¿LLEGA HOLLOW KNIGHT SILKSONG A PS4, PS5 Y XBOX?"}
    Cuerpo={"cuerpo1": " Hollow Knight llegó a una gran audiencia desde su lanzamiento para PC en 2017, y acumuló aún más seguidores con sus increíbles puertos de consola,  incluido Nintendo Switch, en 2018. Desde la mente del desarrollador australiano Team Cherry, el Metroidvania infestado de errores en un juego brutal. pero uno con un combate y una exploración increíblemente gratificantes. Cuando originalmente era un proyecto de Kickstarter, Team Cherry prometió contenid adicional para el juego que te permitiría controlar al personaje Hornet, que aparece como una especie de antagonista en Hollow Knight. Bueno, mientras trabajaban lentamente en el DLC Hornet, Team Cherry quería agregar más contenido de lo planeado originalmente, eventualmente convirtiéndolo en su propio juego separado, llamado Hollow Knight Silksong . Entonces, ¿cuándo es la fecha delanzamiento de Hollow Knight Silksong ? En su tráiler de revelación original, Team Cherry anunció que su objetivo era lanzar Hollow Knight Silksong en 2019. Bueno, es posible que hayas notado que eso fue hace un tiempo, y aún no tenemos el juego, entonces, ¿qué pasó? Team Cherry es un estudio muy pequeño, con solo tres o cuatro miembros permanentes del personal, por lo que los eventos mundiales obvios los golpean más fuerte que en cualquier otro lugar, y Hollow Knight Silksong claramente se ha detenido.",
    "cuerpo2":"  Por lo que podemos decir, deberíamos obtener más información sobre Hollow Knight Silksong a principios de 2022. Teniendo en cuenta que Team Cherry reveló el original para Nintendo Switch en una presentación de Nintendo Direct (la presentación de Nintendo E3 2018 para ser exactos), no es descabellado asumir que Habrá que esperar hasta un Nintendo Direct completo para finalmente tener una fecha de lanzamiento. Con suerte, no tendremos que esperar mucho más y podremos obtener detalles concretos sobre la fecha de lanzamiento de Hollow Knight Silksong a principios de 2022.",
    "cuerpo3":" Se ha confirmado que Nintendo Switch es una de las muchas plataformas en las que se lanzará Hollow Knight Silksong. Si sigue el patrón de lanzamiento del Hollow Knight original, probablemente será exclusivo de la consola Nintendo Switch durante varios meses, antes de llegar a otras plataformas.",
    "cuerpo4":"En este momento, Hollow Knight: Silksong solo está oficialmente confirmado para llegar a Nintendo Switch y PC. Es probable que esto cambie después del lanzamiento, pero no espere que llegue a otras plataformas el día del lanzamiento. Esa es toda la información que tenemos actualmente sobre Hollow Knight Silksong hasta ahora, pero con suerte, no pasará mucho tiempo antes de que tengamos más. Si necesita algo para jugar y hacer que la espera sea más llevadera, consulte nuestra guía de los mejores juegos Switch Metroidvania para mantener sus pulgares ocupados."}
    
    Imagenes={  "img1":"/static/PrayTheNews/img_noticia/img/Hollow-Knight-Silksong.jpg",
                "img2":"/static/PrayTheNews/img_noticia/img/Promo_04.webp",
                "img3":"/static/PrayTheNews/img_noticia/img/silksong.jpg",
                "img4":"/static/PrayTheNews/img_noticia/img/EGeoR8IUUAIcdfA.jpg"}
    return render(request, 'PrayTheNews/NoticiasIndividuales.html', Titulos, Cuerpo, Imagenes)