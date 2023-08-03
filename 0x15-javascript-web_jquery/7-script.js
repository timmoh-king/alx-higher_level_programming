#!/usr/bin/node

/*
 * Write a JavaScript script that fetches the character name from this URL:
 * https://swapi-api.alx-tools.com/api/people/5/?format=json
 * The name must be displayed in the HTML tag DIV#character
 */

const character = $('#character');
const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
	character.text(data.name);
});
