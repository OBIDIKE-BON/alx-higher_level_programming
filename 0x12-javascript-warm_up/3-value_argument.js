#!/usr/bin/node
const args = process.argv;
const size = args.length;
if (size >2) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
