// https://www.codewars.com/kata/540c33513b6532cd58000259/train/javascript

// Passed

function sum(...args) {
  let result = args.reduce((a, b) => a + b, 0);
  return result;
}

const output = sum(5, 7, 9);
console.log(output);