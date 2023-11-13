#!/usr/bin/node
const args = process.argv;
function factorial(val) {
  return val === 0 || isNaN(val) ? 1 : val * factorial(val - 1);
}
console.log(factorial(parseInt(args[2])));
