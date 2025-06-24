// https://www.codewars.com/kata/546e2562b03326a88e000020/train/javascript

// Passed

function squareDigits(num) {
  const digits = String(num)
    .split("")
    .map((digit) => Number(digit));
  const squares = digits.map((digit) => digit ** 2);
  const result = Number(squares.map((square) => String(square)).join(""));
  return result;
}

const output = squareDigits(3212);
console.log(output);