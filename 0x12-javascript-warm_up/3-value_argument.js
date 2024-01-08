#!/usr/bin/node
const argValue = process.argv[2];

if (!argValue) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
