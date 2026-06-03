// https://www.codewars.com/kata/5720a1cb65a504fdff0003e2/train/javascript

// Passed

function differenceInAges(ages) {
  let sortedAges = ages.sort((a, b) => a - b);
  let youngestAge = sortedAges[0];
  let oldestAge = sortedAges[sortedAges.length - 1];
  let result = [youngestAge, oldestAge, oldestAge - youngestAge];
  return result;
}

const output = differenceInAges([82, 15, 6, 38, 35]);
console.log(output);