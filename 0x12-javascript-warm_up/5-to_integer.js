#!/usr/bin/node
const firstArgument = process.argv[2];
const intvalue = parseInt(firstArgument);
if (!isNaN(intvalue)) {
  console.log(`My number: ${intvalue}`);
} else {
  console.log('Not a number');
}
