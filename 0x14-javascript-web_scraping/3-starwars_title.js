#!/usr/bin/node
// Import the request module
const request = require('request');

// Construct the API URL
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

// Make the GET request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
