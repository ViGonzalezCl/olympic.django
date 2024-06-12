$(document).ready(function() {
  $("#crear-usuario-form").validate({
    rules: {
      nombre: {
        required: true,
        minlength: 3,
        maxlength: 50
      },
      apellido: {
        required: true,
        minlength: 3,
        maxlength: 50,

      },
      email: {
        required: true,
        email: true,
        maxlength: 40
      },
      password: {
        required: true,
        minlength: 8
      },
      confirm_password: {
        required: true,
        equalTo: "#password"
      },
      direccion: {
        required: true,
        maxlength: 30
      },
      region: {
        required: true
      },
      terminos: {
        required: true
      }
    },
    messages: {
      nombre: {
        required: "Por favor ingrese su nombre",
        minlength: "Su nombre debe tener al menos 3 caracteres",
        maxlength: "Su nombre no debe exceder los 50 caracteres",
        pattern: "Solo se permiten letras y espacios"      },
      apellido: {
        required: "Por favor ingrese sus apellidos",
        minlength: "Sus apellidos deben tener al menos 3 caracteres",
        maxlength: "Sus apellidos no deben exceder los 50 caracteres",
        pattern: "Solo se permiten letras y espacios"      },
      email: {
        required: "Por favor ingrese su correo electrónico",
        email: "Por favor ingrese un correo electrónico válido",
        maxlength: "Su correo electrónico no debe exceder los 100 caracteres"
      },
      password: {
        required: "Por favor ingrese una contraseña",
        minlength: "Su contraseña debe tener al menos 6 caracteres",
        maxlength: "Su contraseña no debe exceder los 8 caracteres"
      },
      confirm_password: {
        required: "Por favor confirme su contraseña",
        equalTo: "La contraseña no coincide"
      },
      direccion: {
        required: "Por favor ingrese su dirección",
        maxlength: "Su dirección no debe exceder los 30 caracteres"
      },
      region: {
        required: "Por favor seleccione una región"
      },
      terminos: {
        required: "Debe aceptar los términos y condiciones"
      }
    }
  });
  // previene que se mande la cosa al apretar enter sin que esten comppletos los datos
  $("#crear-usuario-form").on("keypress", function(event) {
    if (event.which === 13) {
      event.preventDefault();
      if ($(this).valid()) {
        //pero si esta listo, se envia 
        $(this).submit();
      }
    }
  });

});