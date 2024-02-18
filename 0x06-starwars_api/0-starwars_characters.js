#!/usr/bin/node

const request = require('request');
const argv = require('node:process').argv;

function printChartersName (arrayName) {
  if (!arrayName.length) { return; }

  request(arrayName[0], function (error, resp, body) {
    if (error) {
      console.error(error);
      return;
    }
    const characterBody = JSON.parse(body);
    if (characterBody) { console.log(characterBody.name); }
    printChartersName(arrayName.slice(1));
  });
}

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}/`, function (error, resp, body) {
  if (error) {
    console.error(error);
    return;
  }

  const charactersUrl = JSON.parse(body).characters;
  printChartersName(charactersUrl);
});
