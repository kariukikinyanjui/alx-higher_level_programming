/* global $ */
$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();

    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}',
      type: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function () {
        $('#hello').text('Error fetching translation');
      }
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});
