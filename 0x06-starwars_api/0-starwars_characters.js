#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printChar(characters, 0);
  }
});

function printChar (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChar(characters, index + 1);
      }
    }
  });
}
