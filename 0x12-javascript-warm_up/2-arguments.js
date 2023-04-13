#!/usr/bin/node
const count = process.argv.length;

let myVar;
if (count === 2) {
  myVar = 'No argument';
} else if (count === 3) {
  myVar = 'Argument found';
} else {
  myVar = 'Arguments found';
}
console.log(myVar);
