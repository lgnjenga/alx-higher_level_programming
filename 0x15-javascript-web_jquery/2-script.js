// 2-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Select the <div> with id "red_header" and attach a click event
  $("#red_header").click(function () {
    // Inside the click event, select the <header> element and update its text color to red
    $("header").css("color", "#FF0000");
  });
});
