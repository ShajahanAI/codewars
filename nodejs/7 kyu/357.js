// https://www.codewars.com/kata/5c942f40bc4575001a3ea7ec/train

// Passed

function per(n) {
  let getDigits = (num) =>
    String(num)
      .split("")
      .map((strDigit) => Number(strDigit));
  let digits = getDigits(n);
  let result = [];
  while (digits.length > 1) {
    n = digits.reduce((prev, curr) => prev * curr, 1);
    digits = getDigits(n);
    result.push(n);
  }

  return result;
}

const output = per(10);
console.log(output);