// https://www.codewars.com/kata/551186edce486caa61000f5c/train/javascript

// Passed

function countSquares(n, memo = {}) {
  if (n === 1) return 1;

  if (n in memo) {
    return memo[n];
  }

  let result = countSquares(n - 1, memo) + n ** 2;
  memo[n] = result;
  return result;
}

const output = countSquares(8);
console.log(output);