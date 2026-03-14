// https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/javascript

// Passed

function sumOfDifferences(arr) {
  let sortedArr = arr.sort((a, b) => b - a);
  let totalSum = 0;
  for (let idx = 0; idx < sortedArr.length - 1; idx++) {
    totalSum += sortedArr[idx] - sortedArr[idx + 1];
  }
  return totalSum;
}

const output = sumOfDifferences([1, 2, 10]);
console.log(output);