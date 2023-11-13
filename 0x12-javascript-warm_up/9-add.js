#!/usr/bin/node
function add (a, b) {
  const result = a + b;
  return result;
}
const argument1 = parseInt(process.argv[2]);
const argument2 = parseInt(process.argv[3]);

if (!isNaN(argument1) && !isNaN(argument2)) {
  console.log(add(argument1, argument2));
} else {
  console.log('NaN');
}
