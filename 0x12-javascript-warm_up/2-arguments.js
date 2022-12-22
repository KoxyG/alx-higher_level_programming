#!/usr/bin/node
/*
argc is always more than the number of command line argument
if one argument is expected argc should be = 2
*/
const argc = process.argv.length

if (argc === 2) {
    console.log('No argument');
} else if (argc === 3) {
    console.log('Argument found');
} else {
    console.log('Argument found');
}
