#!/usr/bin/node
const request = require('request');
const allurl = process.argv[2];
request.get(allurl, (err, response, body) => {
  let count = 0
  if (err) {
    console.log(err);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    data.results.forEach(film => {
      if(film.characters.includes("https://swapi-api.alx-tools.com/api/people/18/")) {
        count += 1;
      }
    });
  }
    console.log(count);
    
});
