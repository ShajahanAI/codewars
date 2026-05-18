// https://www.codewars.com/kata/5497a3c181dd7291ce000700/train/javascript

// Passed

function diagonalSum(matrix) {
  let diagonalNumbers = matrix.map((row, idx) => row[idx]);
  let sum = diagonalNumbers.reduce((a, b) => a + b, 0);
  return sum;
}

const output = diagonalSum([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]);
console.log(output);