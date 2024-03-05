// 5-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Select the <div> with id "add_item" and attach a click event
  $("#add_item").click(function () {
    // Inside the click event, append a new <li> element to the <ul> with class "my_list"
    $(".my_list").append("<li>Item</li>");
  });
});
