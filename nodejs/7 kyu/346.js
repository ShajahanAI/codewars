// https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/javascript

// Passed

function smaller(nums) {
  let result = nums.map(
    (num, idx) =>
      nums.slice(idx + 1).filter((rightNum) => rightNum < num).length,
  );
  return result;
}

const output = smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]);
console.log(output);