#!/usr/bin/node
// Import the file system module
const fs = require('fs');

// Getting file path and string to write
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write to file
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Content has been written to ' + filePath);
  }
});
