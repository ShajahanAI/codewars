// https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/javascript

// Passed

function digitize(n) {
  let digits = String(n)
    .split("")
    .map((digit) => Number(digit));
  return digits;
}

const output = digitize(8675309);
console.log(output);