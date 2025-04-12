// https://www.codewars.com/kata/52f3149496de55aded000410/train/javascript

// Passed

function sumDigits(number) {
  const digits = String(number)
    .split("")
    .filter((digit) => digit !== "-");
  let sumOfDigits = digits
    .map((digit) => Number(digit))
    .reduce((prev, curr) => prev + curr);
  return sumOfDigits;
}


const output = sumDigits(8932);
console.log(output);