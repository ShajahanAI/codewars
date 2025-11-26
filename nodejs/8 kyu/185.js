// https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/javascript

// Passed

function sum(numbers) {
  return numbers.reduce((prev, curr) => prev + curr, 0);
}

const output = sum([1, 5.2, 4, 0, -1]);
console.log(output);