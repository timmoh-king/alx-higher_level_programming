#!/usr/bin/node

/*
 * Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item
 * The new element must be: <li>Item</li>
 * The new element must be added to UL.my_list
 */

const addItem = $('#add_item');
const myList = $('ul.my_list');

addItem.on('click', function () {
  const newElement = $('<li></li>').text('Item');
  myList.append(newElement);
});
