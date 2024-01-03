#!/usr/bin/node
// Import the request module
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];
// Make the GET request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;

    // Filter films where character ID 18 is present
    const filmsWithWedge = filmsData.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/films/' + process.argv[18] + '/'));

    console.log(filmsWithWedge.length);
  }
});
