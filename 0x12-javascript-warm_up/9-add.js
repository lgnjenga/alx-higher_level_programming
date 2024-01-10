#!/usr/bin/node
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(x, y);
