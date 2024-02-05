#!/opt/homebrew/bin/node
function factorial (n) {
  let p = 1;
  for (let i = 1; i <= n; i++) {
    p *= i;
  }
  return p;
}
console.log(factorial((process.argv[2])));
