// 6-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Select the <div> with id "update_header" and attach a click event
  $("#update_header").click(function () {
    // Inside the click event, select the <header> element and update its text
    $("header").text("New Header!!!");
  });
});
