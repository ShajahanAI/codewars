// https://www.codewars.com/kata/593c9175933500f33400003e/train/javascript

// Passed

function multiples(m, n) {
  let result = [];
  for (let i = 1; i < m + 1; i++) {
    result.push(n * i);
  }
  return result;
}

const output = multiples(3, 5);
console.log(output);