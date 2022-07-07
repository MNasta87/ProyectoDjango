
const btnEnviar = document.getElementById('submit');
const Terminos = document.getElementById('Terminos')

const correo = document.getElementById('correo')
const usuario = document.getElementById('usuario')
const nombre = document.getElementById('nombre')
const contra = document.getElementById('password')
const contra2 = document.getElementById('password2')

const ExpRegNomUsuario=/^[a-z0-9_-]{3,16}$/;
const Expcorreo = /^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$/i;  

  const validar = ()=> {
    const contraVa = contra.value.trim() // con el value tomamos el valor y el trim borramos los espacion en blanco del principio
    const contra2Va = contra2.value.trim()

    
    const correoVa = correo.value.trim()
    const usuarioVa = usuario.value.trim()
    const nombreVa = nombre.value.trim()
    
    Pasa = true;
    //Email
    if(correoVa == ''){
      validaFalla(correo,'No puede estar en Blanco')
      Pasa = false;

    }

    else if (!Expcorreo.test(correoVa)){

      validaFalla(correo,'Correo no valido')
      Pasa = false;
    }
    else if (usuarioVa.length > 40){
      validaFalla(usuario,'Debe Cumplir con el maximo de caracteres')
      Pasa = false;
    }
    else{
      validaOk(correo,'')}


    //Nick
    if(usuarioVa == ''){
      validaFalla(usuario,'No puede estar en Blanco')
      Pasa = false;

    }
    else if (usuarioVa.length < 4 || usuarioVa.length > 15){
      validaFalla(usuario,'Debe Cumplir con el minimo y maximo de caracteres')
      Pasa = false;
    }
    else if(usuarioVa.match(ExpRegNomUsuario) ==null){
      
      validaFalla(usuario,'Debe Cumplir con los caracteres permitidos')
      Pasa = false;

    }
    else{
      validaOk(usuario,'')}



    //Nombre Usuario
    if(nombreVa == ''){
      validaFalla(nombre,'No puede estar en Blanco')
      Pasa = false;

    }
    else if (nombreVa.length < 3 || nombreVa.length > 40){
      validaFalla(nombre,'Debe Cumplir con el minimo y maximo de caracteres')
      Pasa = false;
    }
    else{
      validaOk(nombre,'')}


    //Terminos de condicion
    if(!document.getElementById('Terminos').checked){
      validaFalla(Terminos,'Acepte antes de continuar.')
      Pasa = false;
    }else{
      validaOk(Terminos,'')
    }


    //Contra
    if(contraVa == ''){
        validaFalla(contra,'No puede estar en Blanco')
        Pasa = false;
      }
    else if(contraVa.length < 4 ){
      validaFalla(contra,'No puede Tener menos de 4 caracteres')
      Pasa = false;
    }
    else if(contraVa.length > 16 ){
      validaFalla(contra,'No puede Tener mas de 16 caracteres')
      Pasa = false;
    }
    else{
      validaOk(contra,'')}

    //contra 2 
    
    if(contra2Va == ''){
      validaFalla(contra2,'No puede estar en Blanco')
      Pasa = false;
    }   
    else if(contraVa !== contra2Va){
      validaFalla(contra2,'ERROR. Las contraseñas no son iguales.')
      Pasa = false;
    }
    
    else{
      validaOk(contra2,'')

    }


    if(Pasa){
      document.formulario.submit();
    }
    else{
      return 0;
    }

    
  }

  const validaFalla = (input,mensaje) => {
    const formControl = input.parentElement
    const aviso = formControl.querySelector('p')
    aviso.innerText = mensaje
    formControl.className = 'formulario__grupo-input falla'
  }

  const validaOk = (input,mensaje) => {
    const formControl = input.parentElement
    const aviso = formControl.querySelector('p')
    aviso.innerText = mensaje
   
  }








