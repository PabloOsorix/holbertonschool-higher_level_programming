const $ = window.$;
$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr',
    function (data) {
      $('#hello').append(data.hello);
    });
});
