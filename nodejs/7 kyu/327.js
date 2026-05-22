// https://www.codewars.com/kata/5806c2f897dba05dd900004c/train/javascript

// Passed

function magnitude(vector) {
  let squareSum = vector.map((val) => val ** 2).reduce((a, b) => a + b, 0);
  let result = squareSum ** 0.5;
  return result;
}

const output = magnitude([-2, -4, 4]);
console.log(output);