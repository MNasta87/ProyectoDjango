function commentBox() {
	var name = document.getElementById('name').value;
	var comment = document.getElementById('comment').value;


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


	

	if (name == "" || comment == "") {
		alert("Porfavor introduce la informacion requerida!");
	}
	else if(comment == "Mierda"){
		alert("La palabra escrita no está permitida")

	}


	else {
		var parent = document.createElement('div');
		var el_name = document.createElement('h6');
		var el_message = document.createElement('p');
		var el_line = document.createElement('hr');
		var txt_name = document.createTextNode(name);
		var txt_message = document.createTextNode(comment);
		el_name.appendChild(txt_name);
		el_message.appendChild(txt_message);
		el_line.style.border = '1px solid #000';
		parent.appendChild(el_name);
		parent.appendChild(el_line);
		parent.appendChild(el_message);
		parent.setAttribute('class', 'pane');
		document.getElementById('result').appendChild(parent);

		document.getElementById('name').value = "";
		document.getElementById('comment').value = "";
	}

}

