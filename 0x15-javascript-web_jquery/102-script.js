/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + $('#languageCode').val(), function (data) {
      $('#hello').text(data.hello);
    });
  });
});
