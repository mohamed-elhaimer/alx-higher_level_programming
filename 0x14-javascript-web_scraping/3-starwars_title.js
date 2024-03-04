#!/usr/bin/node
const request = require('request');
const episodeNumber = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + episodeNumber, function (error, response, body) {
  if (error) { console.log(error); } else if (response.statusCode === 200) {
    const responseJson = JSON.parse(body);
    console.log(responseJson.title);
  } else {
    console.log('Error code: ', response.statusCode);
  }
});
