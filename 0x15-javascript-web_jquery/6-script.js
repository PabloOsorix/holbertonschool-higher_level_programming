const $ = window.$;
$(document).ready(function () {
  $('#update_header').on('click', function () {
    $('header').empty().append('New Header!!!');
  });
});
