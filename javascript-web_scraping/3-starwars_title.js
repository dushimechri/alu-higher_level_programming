#!/usr/bin/node
const request = require('request');
const epnumber = process.argv[2];
const allurl = `https://swapi-api.alx-tools.com/api/films/${epnumber}`
request.get(allurl, (err, response, body) => {
  if (err) {
    console.log(err); 
}
if (response.statusCode === 200) {
  const data = JSON.parse(body);
  console.log(data.title);
}
});
