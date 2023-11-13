#!/usr/bin/node
const args = process.argv;
let times = parseInt(args[2]);
if (!isNaN(times)) {
  while (times > 0) {
    console.log('C is fun');
    times--;
  }
} else {
  console.log('Missing number of occurrences');
}
