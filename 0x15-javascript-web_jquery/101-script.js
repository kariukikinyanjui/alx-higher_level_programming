/* global $ */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('<li>Item</li>').appendTo('UL.my_list');
  });

  $('#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
