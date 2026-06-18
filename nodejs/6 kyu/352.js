// https://www.codewars.com/kata/541c8630095125aba6000c00/train/javascript

// Passed

function digitalRoot(n) {
  let digits = String(n)
    .split("")
    .map((strDigit) => Number(strDigit));
  if (digits.length > 1) {
    let newNumber = digits.reduce((prev, curr) => prev + curr, 0);
    return digitalRoot(newNumber);
  }

  let result = digits[0];
  return result;
}

const output = digitalRoot(456);
console.log(output);