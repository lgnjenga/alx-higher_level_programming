// 7-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Fetch data from the given URL using jQuery's AJAX
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    method: "GET",
    dataType: "json",
    success: function (data) {
      // Update the text of the <div> with id "character" with the character name
      $("#character").text(data.name);
    },
    error: function (error) {
      // Handle errors if the request fails
      console.error("Error fetching data:", error);
    },
  });
});
