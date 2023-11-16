#!/usr/bin/node
const { dict } = require('./101-data');

const occurrencesByUserId = {};
for (const userId in dict) {
  const occurrences = dict[userId];

  if (occurrences in occurrencesByUserId) {
    occurrencesByUserId[occurrences].push(userId);
  } else {
    occurrencesByUserId[occurrences] = [userId];
  }
}

console.log(occurrencesByUserId);
