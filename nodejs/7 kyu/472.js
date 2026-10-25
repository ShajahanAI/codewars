// https://www.codewars.com/kata/59d28768a25c8c51a6000057/train/javascript

// Passed

function calc_ms(n) {
  let result = Number(String(2 ** n) + "0".repeat(n));
  return result;
}

const output = calc_ms(6);
console.log(output);