#!/usr/bin/node
const fs = require('fs');
const argvs = process.argv[2];
fs.readFile(argvs, 'utf-8', (err, data) => {
  if (err){
    console.log(err);
  }
  console.log(data)
  
})
