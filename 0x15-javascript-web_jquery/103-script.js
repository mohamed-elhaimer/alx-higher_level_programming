document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(() => {
    const val = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + val,
      success: function (data) {
        $('div#hello').html(data.hello);
      }
    });
  });
  $('input#language_code').focus(function () {
    $('input#language_code').keypress(function (event) {
      if (event.which === 13) {
        const val = $('input#language_code').val();
        $.ajax({
          type: 'GET',
          url: 'https://hellosalut.stefanbohacek.dev/?lang=' + val,
          success: function (data) {
            $('div#hello').html(data.hello);
          }
        });
      }
    });
  });
});
