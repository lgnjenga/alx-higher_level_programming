// 9-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Fetch data from the given URL using jQuery's AJAX
  $.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: "GET",
    dataType: "json",
    success: function (data) {
      // Update the text of the <div> with id "hello" with the fetched translation
      $("#hello").text(data.hello);
    },
    error: function (error) {
      // Handle errors if the request fails
      console.error("Error fetching data:", error);
    },
  });
});
