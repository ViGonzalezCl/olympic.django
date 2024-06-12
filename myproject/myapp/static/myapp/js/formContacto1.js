$(document).ready(function () {
    $("#formularioContacto").validate({
        rules: {
            asuntoSelect: {
                required: true
            },

            nombreInput: {
                required: true,
                minlength: 3,
                maxLength: 50
            },

            apellidosInput: {
                required: true,
                minlength: 3,
                maxLength: 50
            },

            emailInput: {
                required: true,
                email: true,
                maxLength: 100
            },

            mensaje: {
                required: true
            }
        },
        messages: {
            asuntoSelect: {
                required: "Por favor, seleccione una opción"
            },
            nombreInput: {
                required: "Por favor, ingrese su nombre",
                minlength: "Debe tener 3 caracteres como mínimo",
                maxLength: "No debe exceder los 50 carácteres",
                pettern: "Solo se permiten letras mayus/min y espacios"
            },
            apellidosInput: {
                required: "Por favor, ingrese sus apellidos",
                minlength: "Debe tener 3 carateres como mínimo",
                maxLength: "No debe exceder los 50 carácteres",
                pettern: "Solo se permiten letras mayus/min y espacios"
            },
            emailInput: {
                required: "Por favor, ingresa tu direccion de correo",
                email: "Ingrese un correo válido",
                maxLength: "Su correo electrónico no debe exceder los 100 caracteres"
            },
        }
    });
});

//Funcion para limpiar campos

function limpiarCampos() {
    $("#formularioContacto")[0].reset();
    $("#formularioContacto").validate().resetForm();
}

//Submit del formulario
$("#formularioContacto").on("submit", function (event) {
    if (!$(this).valid()) {
        event.preventDefault();
    }
});

