document.addEventListener('DOMContentLoaded', function () {
  $('input#btn_translate').click(function () {
    const val = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + val,
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  });
});
