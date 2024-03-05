// 8-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Fetch data from the given URL using jQuery's AJAX
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    dataType: "json",
    success: function (data) {
      // Select the <ul> with id "list_movies"
      var movieList = $("#list_movies");

      // Iterate through each movie and append a new <li> to the <ul> with the movie title
      data.results.forEach(function (movie) {
        movieList.append("<li>" + movie.title + "</li>");
      });
    },
    error: function (error) {
      // Handle errors if the request fails
      console.error("Error fetching data:", error);
    },
  });
});
