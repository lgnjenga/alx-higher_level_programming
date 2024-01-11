#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const [, , fileA, fileB, fileC] = process.argv;

try {
  const dataA = fs.readFileSync(fileA, 'utf8');
  const dataB = fs.readFileSync(fileB, 'utf8');

  fs.writeFileSync(fileC, dataA + dataB);
  console.log(`The content of ${fileA} and ${fileB} has been concatenated and written to ${fileC}`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
