#!/usr/bin/node
const sz = parseInt(process.argv[2]);

if (isNaN(sz) || sz < 1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sz; i++) {
    let r = '';
    for (let j = 0; j < sz; j++) {
      r += 'X';
    }
    console.log(r);
  }
}
