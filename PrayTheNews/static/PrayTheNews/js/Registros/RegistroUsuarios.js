
const btnEnviar = document.getElementById('submit');




  const contra = document.getElementById('password')
  const contra2 = document.getElementById('password2')

  

  const validarContra = ()=> {
    const contraVa = contra.value.trim() // con el value tomamos el valor y el trim borramos los espacion en blanco del principio
    const contra2Va = contra2.value.trim()

    if(contraVa !== contra2Va){
      validaFalla(contra2,'ERROR. Las contraseñas no son iguales.')
      return 0;
    }
    else{
      validaOk(contra2,'')
      document.formulario.submit();
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








