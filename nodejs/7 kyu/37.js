// https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/javascript

// Passed

function evenOrOdd(str) {
  let evenSum = 0;
  let oddSum = 0;
  str.split("").forEach((digit) => {
    digit = Number(digit);
    if (digit % 2 === 0) {
      evenSum += digit;
    } else {
      oddSum += digit;
    }
  });

  if (oddSum === evenSum) return "Even and Odd are the same";
  return oddSum > evenSum
    ? "Odd is greater than Even"
    : "Even is greater than Odd";
}

const output = evenOrOdd('42153');
console.log(output);