// https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/javascript

// Passed

function jumpingNumber(n) {
  let digits = String(n)
    .split("")
    .map((strDigit) => Number(strDigit));
  let isJumpingNumber = digits.every(
    (digit, idx) =>
      idx === digits.length - 1 || Math.abs(digit - digits[idx + 1]) === 1
  );
  let result = isJumpingNumber ? "Jumping!!" : "Not!!";
  return result;
}

const output = jumpingNumber(4343456);
console.log(output);