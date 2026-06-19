// https://www.codewars.com/kata/590938089ff3d186cb00004c/train/javascript

// Passed

function suffixSums(a) {
  let result = [];
  let currentVal = 0;
  for (let idx = a.length - 1; idx >= 0; idx--) {
    currentVal += a[idx];
    result.push(currentVal);
  }

  result = result.reverse();
  return result;
}

const output = suffixSums([1, 123, 23]);
console.log(output);