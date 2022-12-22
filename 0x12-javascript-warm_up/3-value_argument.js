#!/usr/bin/node
// argc is always more than the number of command line argument
// if one argument is expected argc should be = 2

if (process.argv[2] === undefined) {
    console.log('No argument');
} else {
    console.log('process.argv[2]');
}

