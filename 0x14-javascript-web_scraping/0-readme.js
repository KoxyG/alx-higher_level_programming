#!/usr/bin/node

const fs = require('fs')
const filename = process.argv[2]

fs.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
	  console.log('Error');
  }else {
	  console.log('content');
  }
	  
});