#!/usr/bin/node
const fs = require('fs');
const argvs = argv[0];
const erroe_Object = { Error: ENOENT: no such file or directory, open 'doesntexist'
	    at Error (native)
	  errno: -2,
	  code: 'ENOENT',
	  syscall: 'open',
	  path: 'doesntexist' }
fs.open('argvs', 'utf-8', (err, data) => {
  if (err){
    console.log(erroe_Object);
  }
  console.log(data)
  
})
