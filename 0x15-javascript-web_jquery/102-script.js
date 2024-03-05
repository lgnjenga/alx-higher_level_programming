// 102-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Attach a click event to the button with id "btn_translate"
  $("#btn_translate").click(function () {
    // Get the language code from the input with id "language_code"
    var languageCode = $("#language_code").val();

    // Fetch the translation from the API using the entered language code
    $.ajax({
      url: "https://www.fourtonfish.com/hellosalut/hello/",
      method: "GET",
      dataType: "json",
      data: { lang: languageCode },
      success: function (data) {
        // Display the fetched translation in the <div> with id "hello"
        $("#hello").text(data.hello);
      },
      error: function (error) {
        // Handle errors if the request fails
        console.error("Error fetching data:", error);
      },
    });
  });
});
