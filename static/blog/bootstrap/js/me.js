$(document).ready(function (e) {

    $('#contact-form-button').on('click', function (e) {
        e.preventDefault();
        data = $('#contact-form').serializeArray();
        send_form_ajax(data, $('#contact-form-button'));
    });
});

function send_form_ajax(formData, button) {
    $.ajax({
        data: formData,
        url: '/check-form/',
        type: 'post',
        beforeSend: function () {
            button.html("Procesando...");
        },
        success: function (response) {
            button.html('Mensaje Recibido!');
        },
        error: function(response){
            button.html('Ha habido un problema');
        }
    });

}