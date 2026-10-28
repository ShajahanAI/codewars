// https://www.codewars.com/kata/577b9960df78c19bca00007e/train/javascript

// Passed

function findDigit(num, nth) {
  if (nth <= 0) {
    return -1;
  }

  let strAbsNum = String(Math.abs(num));
  let result =
    nth > strAbsNum.length ? 0 : Number(strAbsNum[strAbsNum.length - nth]);
  return result;
}

const output = findDigit(5673, 4);
console.log(output);