// https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/javascript

// Passed

function sumTriangularNumbers(n) {
  let getNthTriangularNumber = (n) => (n * (n + 1)) / 2;
  let result = 0;
  for (let row = 1; row <= n; row++) {
    result += getNthTriangularNumber(row);
  }
  return result;
}

const output = sumTriangularNumbers(34);
console.log(output);