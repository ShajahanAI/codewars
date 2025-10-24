// https://www.codewars.com/kata/5b4e474305f04bea11000148/train/javascript

// Passed

function digits(num) {
  let allDigits = String(num)
    .split("")
    .map((digit) => Number(digit));
  let allSums = [];
  let currentIdx = 0;
  for (const firstDigit of allDigits) {
    for (const secondDigit of allDigits.slice(currentIdx + 1)) {
      let sum = firstDigit + secondDigit;
      allSums.push(sum);
    }

    currentIdx++;
  }

  return allSums;
}

const output = digits(81596);
console.log(output);