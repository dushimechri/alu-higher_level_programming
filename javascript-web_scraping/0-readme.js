#!/usr/bin/node
const fs = require('fs');
const argvs = process.argv[2];
const erroe_Object = {code: 'ENOENT',
  message: 'no such file or directory, open \'doesntexist\'',
  errno: -2,
  syscall: 'open',
  path: 'doesntexist'}
fs.open('argvs', 'utf-8', (err, data) => {
  if (err){
    console.log(erroe_Object);
  }
  console.log(data)
  
})
