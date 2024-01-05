#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    let count = 0;
    results.forEach(function (movie) {
      if (movie.characters.find((character) => character.endsWith('/18/'))) {
        count++;
      }
    });
    console.log(count);
  }
});
