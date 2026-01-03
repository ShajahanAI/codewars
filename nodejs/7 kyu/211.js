// https://www.codewars.com/kata/56aed5db9d5cb55de000001c/train/javascript

// Passed

function twoCount(n) {
  let result = 0;
  while (n % 2 === 0) {
    result++;
    n /= 2;
  }

  return result;
}

const output = twoCount(17280);
console.log(output);