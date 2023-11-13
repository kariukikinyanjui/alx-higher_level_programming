#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  for (let i = 0; i < Math.max(0, size); i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
