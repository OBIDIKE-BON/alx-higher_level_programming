#!/usr/bin/node
const args = process.argv;
try {
  console.log(args[2]);
} catch (err) {
  console.log('No argument');
}
