#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
req(url + id, function (err, response, body) {
  if (!err) {
    const data = JSON.parse(body);
    const ch = data.characters;
    for (const i of ch) {
      req(i, function (error, res, body1) {
        if (!error) {
          const data1 = JSON.parse(body1);
          console.log(data1.name);
        }
      });
    }
  }
});
