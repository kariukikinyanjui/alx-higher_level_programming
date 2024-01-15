/* global $ */
$(document).read(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
