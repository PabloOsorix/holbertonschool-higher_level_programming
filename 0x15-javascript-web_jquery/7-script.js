const $ = window.$;
$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json',
    function (data) {
      $('#character').append(data.name);
    });
});
