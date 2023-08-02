#!/usr/bin/node

/*
 * JavaScript script that adds the class red to the <header> element when the user clicks on the tag
 */
const header = $('header');
const divHeader = $('#red_header');

divHeader.on('click', function () {
  header.addClass('red');
});
