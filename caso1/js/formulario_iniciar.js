$("#main").submit(
    function(){
        var $iniciar = $("#main")
        $.validator.addMethod("espacios", function(value, element){
            return value == ' ' || value.trim().length != 0
        }, "Espacios no son permitidos");
        if($iniciar.length){
            $iniciar.validate({
                rules:{
                    email: {
                        required: true,
                        email: true
                    },
                    password:{
                        required: true,
                        espacios: true,
                        minlength: 5,
                        maxlength: 15
                    }
                },
                messages:{
                    email: {
                        required: 'Correo es obligatorio',
                    },
                    password: {
                        required: 'Contraseña es obligatorio',
                        minlength: 'Debe tener un mínimo de 5 caracteres',
                        maxlength: 'Debe tener un máximo de 15 caracteres',
                    }
                }

            })
        }
        event.preventDefault();
    }
);