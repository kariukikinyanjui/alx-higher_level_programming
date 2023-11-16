#!/usr/bin/node
const fs = require('fs');

const firstArgument = fs.readFileSync(process.argv[2]).toString();
const secondArgument = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], firstArgument + secondArgument);
