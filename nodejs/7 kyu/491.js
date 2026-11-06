// https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/javascript

// Passed

function minValue(values) {
  let uniqueDigits = Array.from(new Set(values));
  let sortedUniqueDigits = uniqueDigits.sort((a, b) => a - b);
  let result = Number(sortedUniqueDigits.map(String).join(""));
  return result;
}

const output = minValue([5, 6, 9, 9, 7, 6, 4]);
console.log(output);