// https://www.codewars.com/kata/596a81352240711f3b00006e/train/javascript

// Passed

function binMul(m, n) {
  let result = [];
  [m, n] = [Math.max(m, n), Math.min(m, n)];

  while (m > 0 && n > 0) {
    if (m % 2 === 1) {
      result.push(n);
    }

    m = Math.floor(m / 2);
    n *= 2;
  }

  result = result.reverse();
  return result;
}

const output = binMul(100, 15);
console.log(output);