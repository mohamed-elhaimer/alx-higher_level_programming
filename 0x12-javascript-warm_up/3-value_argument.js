#!/usr/bin/node
const args = process.argv.slice(2);
if (args[2] == null) {
  console.log('No argument');
} else {
  args.forEach(val => {
    console.log(val);
  });
}
