// https://www.codewars.com/kata/58ca77b9c0d640ecd2000b1e/train/javascript

// Passed

function procedure(n) {
  // getting all multiples till 100
  let multiplesTillHundred = [];
  for (let multiple = n; multiple <= 100; multiple += n) {
    multiplesTillHundred.push(multiple);
  }

  // mapping each multiple to its digit sum
  let getDigitSum = (num) =>
    String(num)
      .split("")
      .map((strDigit) => Number(strDigit))
      .reduce((prev, curr) => prev + curr, 0);
  let multipleDigitSums = multiplesTillHundred.map((multiple) =>
    getDigitSum(multiple),
  );

  // obtaining sum of the digit sums
  let result = multipleDigitSums.reduce((prev, curr) => prev + curr, 0);
  return result;
}

const output = procedure(12);
console.log(output);