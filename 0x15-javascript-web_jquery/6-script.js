#!/usr/bin/node

/*
 * Write a JavaScript script that updates the text of the <header> element to New Header!!!
 * when the user clicks on DIV#update_header
 */

const updateHeader = $("#update_header");
const header = $("header");

updateHeader.on("click", function () {
  const text = "New Header!!!";
  header.text(text);
});
