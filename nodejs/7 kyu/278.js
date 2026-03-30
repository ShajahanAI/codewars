// https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/javascript

// Passed

function reverseNumber(n) {
  let isNegative = n < 0;
  n = Math.abs(n);
  let reversedNum = Number(String(n).split("").reverse().join(""));
  if (isNegative) {
    reversedNum *= -1;
  }

  return reversedNum;
}

const output = reverseNumber(98989898);
console.log(output);