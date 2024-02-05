#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  const ress = +a + +b;
  return ress;
}
const res = add(args[2], args[3]);
console.log(res);
