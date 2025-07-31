// https://www.codewars.com/kata/57193a349906afdf67000f50/train/javascript

// Passed

function magicSum(numbers) {
  let result = numbers
    .filter((num) => String(num).split("").includes("3") && num % 2 === 1)
    .reduce((prev, curr) => prev + curr, 0);
  return result;
}

const output = magicSum([3, 12, 5, 8, 30, 13]);
console.log(output);