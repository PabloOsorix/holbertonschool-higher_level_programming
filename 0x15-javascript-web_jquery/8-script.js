const $ = window.$;
$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json',
    function (data) {
      for (let i = 0; data.results[i] != null; i++) {
        $('#list_movies').append(data.results[i].title + '</br>');
      }
    });
});
