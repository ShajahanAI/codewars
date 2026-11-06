// https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/javascript

// Passed

function solve(n) {
  let denominations = [500, 200, 100, 50, 20, 10];
  let result = 0;
  for (const denomination of denominations) {
    result += Math.floor(n / denomination);
    n %= denomination;
  }

  result = n === 0 ? result : -1;
  return result;
}

const output = solve(770);
console.log(output);