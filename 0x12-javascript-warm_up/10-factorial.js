#!/usr/bin/node
const args = process.argv;
function facto (a) {
  if (isNaN(a)) {
    return 1;
  } else {
    return a * facto(a - 1);
  }
}
const res = facto(args[2]);
console.log(res);
