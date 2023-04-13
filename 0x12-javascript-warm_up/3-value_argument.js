#!/usr/bin/node

let myVar;
if (typeof process.argv[2] === 'undefined') {
  myVar = 'No argument';
} else {
  myVar = process.argv[2];
}
console.log(myVar);
