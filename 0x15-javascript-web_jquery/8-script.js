#!/usr/bin/node

/*
 * Write a JavaScript script that fetches and lists the title for all movies by using this URL
 * https://swapi-api.alx-tools.com/api/films/?format=json
 * All movie titles must be list in the HTML tag UL#list_movies
 */

const listMovies = $("#list_movies");

$.get(
  "https://swapi-api.alx-tools.com/api/films/?format=json",
  function (data) {
    const results = data.results;
    for (i = 0; i < results.length; i++) {
      const title = results[i].title;
      const newElement = $("<li></li>").text(title);
      listMovies.append(newElement);
    }
  }
);
