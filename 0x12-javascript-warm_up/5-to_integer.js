#!/usr/bin/node
// parseInt function converts first argument to a string
// then returns an integer or NaN
// use of backticks for variable expression
console.log(parseInt(process.argv[2])
  ? `My number: ${parseInt(process.argv[2])}` : 'Not a numer');

