// https://www.codewars.com/kata/55afed09237df73343000042/train/javascript

// Passed

function isLucky(n) {
  let digits = String(n)
    .split("")
    .map((strDigit) => Number(strDigit));
  let digitsSum = digits.reduce((prev, curr) => prev + curr, 0);
  let result = digitsSum === 0 || digitsSum % 9 === 0;
  return result;
}

const output = isLucky(1892376);
console.log(output);