// https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/javascript

// Passed

function solution(nums) {
  let result = nums ? nums.sort((a, b) => a - b) : [];
  return result;
}

const output = solution([1, 2, 3, 10, 5]);
console.log(output);