// https://www.codewars.com/kata/511f11d355fe575d2c000001/train/javascript

// Passed

function twoOldestAges(ages) {
  let sortedAges = ages.sort((a, b) => a - b);
  let agesToReturn = sortedAges.slice(sortedAges.length - 2);
  return agesToReturn;
}

const output = twoOldestAges([1, 5, 87, 45, 8, 8]);
console.log(output);