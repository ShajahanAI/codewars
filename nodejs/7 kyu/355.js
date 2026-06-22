// https://www.codewars.com/kata/66cdc6ab9e7a9f009e0ca8f6/train/javascript

// Passed

function canSnailReachEnd(length, speed, lengthIncreases) {
  let distCoveredInAYear = speed * 365 * 24 * 60;
  let lengthInAYear = length + lengthIncreases * 365 * 24 * 60;
  let result = distCoveredInAYear > lengthInAYear;
  return result;
}

const output = canSnailReachEnd(10, 2, 1);
console.log(output);