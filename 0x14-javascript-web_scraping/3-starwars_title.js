#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
request(url, function (error, response) {
  console.log(error || JSON.parse(response.body).title);
});
