// https://www.codewars.com/kata/5515395b9cd40b2c3e00116c/train/javascript

// Passed

function regression_line(x, y) {
  let sumArr = (arr) => arr.reduce((prev, curr) => prev + curr, 0);
  let xiSum = sumArr(x);
  let yiSum = sumArr(y);

  let xiSquaredSum = sumArr(x.map((num) => num ** 2));

  let xiYiSum = sumArr(x.map((num, idx) => x[idx] * y[idx]));

  let a =
    (xiSquaredSum * yiSum - xiSum * xiYiSum) /
    (x.length * xiSquaredSum - xiSum ** 2);
  let b =
    (x.length * xiYiSum - xiSum * yiSum) /
    (x.length * xiSquaredSum - xiSum ** 2);
  let roundToFourDecimals = (num) => Math.round(num * 10 ** 4) / 10 ** 4;
  let result = [roundToFourDecimals(a), roundToFourDecimals(b)];

  return result;
}

const output = regression_line(
  [25, 30, 35, 40, 45, 50],
  [78, 70, 65, 58, 48, 42],
);
console.log(output);