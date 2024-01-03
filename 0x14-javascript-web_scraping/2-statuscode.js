#!/usr/bin/node
// Import the request module
const request = require('request');

// Get the URL from command line arguments
const url = process.argv[2];

// Make the GET request
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
