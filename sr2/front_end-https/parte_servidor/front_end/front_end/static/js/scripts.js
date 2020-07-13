$(document).ready(function(){
    setInterval(
        function(){
            $('#seccionRecargar').load('/recursos/')
        },5000
    );
});
