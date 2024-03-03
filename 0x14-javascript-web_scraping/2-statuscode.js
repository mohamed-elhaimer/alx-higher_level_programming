#!/usr/bin/node
fetch(process.argv[2], {
  method: 'GET'
})
  .then(response => {
    console.log('code: ', response.status);
  });
