// https://www.codewars.com/kata/588422ba4e8efb583d00007d/train/javascript

// Passed

function lateRide(n) {
  let hours = Math.floor(n / 60);
  let minutes = n - hours * 60;
  let getNumberDigitsSum = (num) =>
    Array.from(String(num))
      .map((strDigit) => Number(strDigit))
      .reduce((prev, curr) => prev + curr, 0);

  let result = getNumberDigitsSum(hours) + getNumberDigitsSum(minutes);
  return result;
}

const output = lateRide(1439);
console.log(output);