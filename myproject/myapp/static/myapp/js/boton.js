function buttonClickHandlers() {
  $('#btn_guardar').click(function(e) {
    e.preventDefault();
    if ($('#formulario').valid()) {
      Swal.fire({
        title: "Su cuenta ha sido creada con exito!",
        icon: "success"
      });
    }
  });

  $('#btn_cancelar').click(function(e) {
    Swal.fire({
      title: "¿Estás seguro que deseas salir?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "Salir"
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.replace("index.html"); // Redirect to index.html
      }
    });
  });
}

$(document).ready(function() {
  buttonClickHandlers();
});