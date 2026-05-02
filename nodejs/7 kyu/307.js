// https://www.codewars.com/kata/556196a6091a7e7f58000018/train/javascript

// Passed

function largestPairSum(numbers) {
  let sortedArr = numbers.sort((a, b) => b - a);
  let largestPairSum = sortedArr[0] + sortedArr[1];
  return largestPairSum;
}

const output = largestPairSum([10, 14, 2, 23, 19]);
console.log(output);