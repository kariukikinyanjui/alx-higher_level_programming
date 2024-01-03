#!/usr/bin/node
// Import the request module
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make the GET Request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksByUser = {};
    // Loop through tasks and count completed tasks for each user
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });
    console.log(completedTasksByUser);
  }
});
