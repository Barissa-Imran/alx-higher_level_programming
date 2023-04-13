#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));

let myVar;
if (isNaN(num)) {
  myVar = 'Not a number';
} else {
  myVar = `My number: ${num}`;
}
console.log(myVar);
