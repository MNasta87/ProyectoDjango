
function filtro(){  
    var grocerias = ["puta", "puto","marica","pirobo","gonorrea"]
    var nodo = document.getElementById("comment").elements["texto"]
    var textarea = nodo.value;
    for(var i = 0; i < grocerias.length;i++){
        regex = new RegExp("(^|\\s)"+grocerias[i]+"($|(?=\\s))","gi")
        textarea = textarea.replace(regex, function($0, $1){return $1 + "#4@!@"});
    }
    nodo.value = textarea;
}