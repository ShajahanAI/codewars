// https://www.codewars.com/kata/5acc3634c6fde760ec0001f7/train/javascript

// Passed

function solve(nums, div) {
  let result = nums.map((num) => num + (num % div));
  return result;
}

const output = solve([33, 23, 45, 78, 65], 10);
console.log(output);