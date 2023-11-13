#!/usr/bin/node
const args = process.argv;
let times = parseInt(args[2]);
if (!isNaN(times)) {
  while (times > 0) {
    let iner = parseInt(args[2]);
    let line = '';
    while (iner > 0) {
      line += 'X';
      iner--;
    }
    console.log(line);
    times--;
  }
} else {
  console.log('Missing size');
}
