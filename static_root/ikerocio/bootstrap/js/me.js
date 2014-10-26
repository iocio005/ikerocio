$(document).ready(function (e) {

    $('#contact-form-button').on('click', function (e) {
        e.preventDefault();
        data = $('#contact-form').serializeArray();
        if (checkForm(data)) {
            send_form_ajax(data, $('#contact-form-button'));
        }
    });
});
function checkForm() {
    patName = new RegExp('[a-zA-Z\ ]+');
    patEmail = new RegExp('[a-zA-Z\.\_\]+@[a-zA-Z]+.[a-zA-Z]+');
    patContent = new RegExp('\w*');
    errorMessage = '';
    if (!patName.test($('#contact-name').val())) {
        $('#contact-form-button').html('¡Pon tu nombre!');
        return false;
    } else if (!patEmail.test($('#contact-mail').val())) {
        $('#contact-form-button').html('¿Se te ha olvidado colocar un mail que exista?');
        return false;
    } else if (!patContent.test($('#contact-message').val())) {
        $('#contact-form-button').html('¿No vas a escribirme nada?');
        return false;
    } else {
        return true;
    }
}
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
        error: function (response) {
            button.html('Ha habido un problema');
        }
    });

}