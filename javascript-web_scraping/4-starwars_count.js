#!/usr/bin/node
const request = require('request');
const allurl = process.argv[2];
request.get(allurl, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const cur = data.characters[16];
    request.get(cur, (err, response, body) => {
      if (err) {
        console.log(err);
    }
      if (response.statusCode === 200) {
      const dataa = JSON.parse(body);
      console.log(dataa.films.length);
    }
    }
    }
});
