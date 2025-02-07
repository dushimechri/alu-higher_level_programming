#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const web = process.argv[2];
const dest = process.argv[3];
request.get(web, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  if (response.statusCode === 200) {
    fs.writeFile(dest, body, 'utf8' ,(err) => {
       if (err) {
         console.log(err);
       }
    });
  }
});

