// https://www.codewars.com/kata/5a512f6a80eba857280000fc/train/javascript

// Passed

function nthSmallest(arr, pos) {
  let sortedArr = arr.sort((a, b) => a - b);
  result = sortedArr[pos - 1];
  return result;
}

const output = nthSmallest([15, 20, 7, 10, 4, 3], 3);
console.log(output);