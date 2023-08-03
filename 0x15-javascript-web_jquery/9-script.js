#!/usr/bin/node

/*
 * Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
 * displays the value of hello from that fetch in the HTML tag DIV#hello
 * The translation of “hello” must be displayed in the HTML tag DIV#hello
 */

const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(apiUrl, function (data) {
  const divHello = $('#hello');
  divHello.text(data.hello);
});
