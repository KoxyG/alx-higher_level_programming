#!/usr/bin/node
// argc is always more than the number of command line argument
// if one argument is expected argc should be = 2

const x = process.argv[2];

if (!parseInt(x)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < x; i++) {
        console.log('C is fun')
    }
}

