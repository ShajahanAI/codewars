// https://www.codewars.com/kata/556021360863a1708900007b/train/javascript

// Passed

function checkValidTrNumber(n) {
  if (typeof n !== "number") {
    return false;
  }

  let digits = String(n)
    .split("")
    .map((strDigit) => Number(strDigit));
  if (digits.length !== 11 || digits[0] === 0) {
    return false;
  }

  let sumOfFirstTenDigits = digits
    .slice(0, 10)
    .reduce((prev, curr) => prev + curr, 0);
  if (sumOfFirstTenDigits % 10 !== digits[10]) {
    return false;
  }

  let calculationResult = 0;
  for (let idx = 0; idx < 9; idx++) {
    if (idx % 2 === 0) {
      calculationResult += digits[idx] * 7;
    } else {
      calculationResult -= digits[idx];
    }
  }

  if (calculationResult % 10 !== digits[9]) {
    return false;
  }

  return true;
}

const output = checkValidTrNumber(36637640050);
console.log(output);