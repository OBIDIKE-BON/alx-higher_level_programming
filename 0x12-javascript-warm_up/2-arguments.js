#!/usr/bin/node
const args = process.argv;
const size = args.length;
if (size === 3) {
  console.log('Argument found');
} else if (size === 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
