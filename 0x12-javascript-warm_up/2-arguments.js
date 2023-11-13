#!/usr/bin/node
const no_arguments = process.argv.length - 2;
if (no_arguments === 0)
{
  console.log("No argument");
}
else if (no_arguments === 1)
{
  console.log("Argument found");
}
else
{
  console.log("Arguments found");
}
