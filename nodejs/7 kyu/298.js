// https://www.codewars.com/kata/570523c146edc287a50014b1/train/javascript

// Passed

function numberJoy(n) {
  let digits = String(n)
    .split("")
    .map((digitStr) => Number(digitStr));
  let digitsSum = digits.reduce((a, b) => a + b, 0);
  let isHarshadNum = n % digitsSum === 0;

  let result = false;
  if (isHarshadNum) {
    let reversedDigitsSum = Number(
      String(digitsSum).split("").reverse().join(""),
    );
    if (reversedDigitsSum * digitsSum === n) {
      result = true;
    }
  }

  return result;
}

const output = numberJoy(1458);
console.log(output);