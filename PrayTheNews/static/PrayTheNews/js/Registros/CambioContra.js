
const Actual = document.getElementById('contra')

const contra = document.getElementById('contra2')
const contra2 = document.getElementById('contra3')


  const validarContra = ()=> {
    const contraVa = contra.value.trim() // con el value tomamos el valor y el trim borramos los espacion en blanco del principio
    const contra2Va = contra2.value.trim()

    const ActualVa = Actual.value.trim()
    
    Pasa = true;
    if(ActualVa == ''){
        validaFalla(Actual,'No puede estar en Blanco')
        Pasa = false;
      }
    else if(ActualVa.length > 16 ){
        validaFalla(Actual,'No puede Tener mas de 16 caracteres')
        Pasa = false;
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
    else if(contraVa == ActualVa ){
        validaFalla(contra,'No puede ser la misma que la contraseña actual.')
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
      document.Cambiarcontra.submit();
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













