$("#registrar").submit(
    function(){
        var $registrar = $("#registrar")
        $.validator.addMethod("espacios", function(value, element){
            return value == ' ' || value.trim().length != 0
        }, "Espacios no son permitidos");
        if($registrar.length){
            $registrar.validate({
                rules:{
                    nombre: {
                        required: true,
                        text: true,
                        espacios: true,
                        minlength: 4,
                        maxlength: 20,
                    },
                    correo: {
                        required: true,
                        email: true
                    },
                    pass:{
                        required: true,
                        espacios: true,
                        minlength: 5,
                        maxlength: 15
                    },
                    confirmar: {
                        required: true,
                        equalTo:'#inputPass',
                        espacios: true,
                        minlength: 5,
                        maxlength: 15
                    }

                },
                messages:{
                    nombre: {
                        required: 'nombre es obligatorio',
                        minlength:'debe tener un mínimo de 4 caracteres',
                        maxlength:'debe tener un máximo de 20 caracteres',
                        text:'Solo se aceptan letras',
                    },
                    correo: {
                        required: 'Correo es obligatorio',
                    },
                    pass: {
                        required: 'Contraseña es obligatorio',
                        minlength: 'Debe tener un mínimo de 5 caracteres',
                        maxlength: 'Debe tener un máximo de 15 caracteres',
                    },
                    confirmar:{
                        required: 'Confirmación es obligatoria',
                        equalTo: 'Debe ingresar la misma contraseña'
                    }
                }

            })
        }
        event.preventDefault();
    }
);