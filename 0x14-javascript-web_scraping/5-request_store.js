#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    fs.writeFileSync(process.argv[3], body);
  }
});
