
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
  });
  
  function validarFormulario(evento) {
    evento.preventDefault();
    var contra = document.getElementById("password").value;
    var contra2 = document.getElementById("password2").value;
    if(contra.value!==contra2.value) {
      alert("Segunda contraseña incorrecta");
      return;
    }
    
    this.submit();
  }




function VContra2(){
    var contra = document.getElementById("password").value;
    var contra2 = document.getElementById("password2").value;
        if (contra.value!==contra2.value){
            alert("Segunda contraseña incorrecta");
         return false;
        }
        else{
        alert("Se envio");
            
            return true;

        }
};
function sumar (){
    alert(aaa)
};