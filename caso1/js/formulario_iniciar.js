$.validator.addMethod("terminaPor", function(value, element, parametro){
    if(value.endsWith(parametro)){
        return true;
    }
    return false;
}, "Debe terminar por {0}" )


$('#main').validate({
    rules: {
        correo: {
            required: true,
            email: true,
            terminaPor: "duoc.cl"
        },
        pass: {
            required: true,
            minlength: 4,
            maxlength: 10
        }
    }
})

$('#iniciar').click(function(){
    if($('#main').valid() == false) {
        return;
    }
    let correo = $('#email').val();
    let pass = $('#password').val();
})