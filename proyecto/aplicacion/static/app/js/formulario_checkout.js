$(document).ready(function() {
    // Capturamos el formulario de compra por medio del ID
    var $form = $("#form_carrito");
  
    // Método creado para evitar los espacios en los inputs
    $.validator.addMethod("espacios", function(value, element) {
      return value.trim().length !== 0;
    }, "Espacios no son permitidos");
  
    // Validamos el formulario de registro campo por campo
    if ($form.length) {
      $form.validate({
        rules: {
          // Parámetros de validación
          nombre: {
            required: true,
            espacios: true,
            minlength: 4,
            maxlength: 20,
            number: false,
          },
          apellido: {
            required: true,
            espacios: true,
            minlength: 4,
            maxlength: 20,
            number: false,
          },
          correo: {
            required: true,
            email: true,
            espacios: true,
          },
          postal: {
            number: true,
          }
        },
  
        // Escribimos los mensajes para que aparezcan cuando los campos sean incorrectos
        messages: {
          nombre: {
            required: 'Nombre es obligatorio',
            minlength: 'Debe tener un mínimo de 4 caracteres',
            maxlength: 'Debe tener un máximo de 20 caracteres',
            text: 'Solo se aceptan letras'
          },
          correo: {
            required: 'Correo es obligatorio'
          }
        }
      });
  
      // Asignar el evento blur a los campos de entrada
      $("#nombre").on("blur", function() {
        $(this).valid(); // Validar el campo al perder el foco
      });
  
      $("#apellido").on("blur", function() {
        $(this).valid(); // Validar el campo al perder el foco
      });
  
      $("#correo").on("blur", function() {
        $(this).valid(); // Validar el campo al perder el foco
      });
    }
  
    // Evitamos que el formulario se envíe por defecto al apretar el botón de continuar
    $form.on("submit", function(event) {
      event.preventDefault();
    });
  });
  