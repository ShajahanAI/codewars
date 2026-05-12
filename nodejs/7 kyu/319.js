// https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1/train/javascript

// Passed

function getAges(sum, difference) {
  let result = null;
  if (sum >= 0 && difference >= 0) {
    let firstAge = (sum - difference) / 2;
    let secondAge = sum - firstAge;
    result = firstAge < 0 || secondAge < 0 ? null : [secondAge, firstAge];
  }

  return result;
}

const output = getAges(24, 4);
console.log(output);