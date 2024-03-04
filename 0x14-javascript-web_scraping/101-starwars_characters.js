#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(url, function (err, response, body) {
  if (!err) {
    const data = JSON.parse(body).characters;
    printCh(data, 0);
  }
});
function printCh (data, index) {
  req(data[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < data.length) {
        printCh(data, index + 1);
      }
    }
  });
}
