// https://www.codewars.com/kata/5545f109004975ea66000086/train/javascript

// Passed

function isDivisible(n, x, y) {
  let result = n % x === 0 && n % y === 0;
  return result;
}

const output = isDivisible(48, 3, 4);
console.log(output);