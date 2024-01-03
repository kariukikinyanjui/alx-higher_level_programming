#!/usr/bin/node
// Import request and fs modules
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make the Get request
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the body content to the specified file in utf-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
