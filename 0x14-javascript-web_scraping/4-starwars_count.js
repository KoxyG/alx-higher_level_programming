#!/usr/bin/node

//A scripts that prints the number of movies
//with a certain character "Wedge Antilles" is present


const request = require('request');
const characterID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/`;
let count = 0;

request.get(url, (error, response, ody) => {
  if (error) {
	  console.log(error);
  } else {
	  const data = JSON.parse(body);
	  data.results.forEach((film) => {
		  film.characters.forEach((character) => {
			  if (character.includes(characterId)) {
				  count += 1
			  }
		  });
	  });
	  console.log(count);
  }
});
