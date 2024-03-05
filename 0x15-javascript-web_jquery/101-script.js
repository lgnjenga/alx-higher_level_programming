// 101-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Add item to the list
  $("#add_item").click(function () {
    $(".my_list").append("<li>Item</li>");
  });

  // Remove last item from the list
  $("#remove_item").click(function () {
    $(".my_list li:last-child").remove();
  });

  // Clear all items from the list
  $("#clear_list").click(function () {
    $(".my_list").empty();
  });
});
