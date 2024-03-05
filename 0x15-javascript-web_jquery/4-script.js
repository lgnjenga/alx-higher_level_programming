// 4-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Select the <div> with id "toggle_header" and attach a click event
  $("#toggle_header").click(function () {
    // Inside the click event, select the <header> element
    var headerElement = $("header");

    // Toggle the class between "red" and "green"
    headerElement.toggleClass("red green");
  });
});
