// https://www.codewars.com/kata/5715eaedb436cf5606000381/train/javascript

// Passed

function positiveSum(arr) {
  let sumVal = arr
    .filter((num) => num > 0)
    .reduce((prev, curr) => prev + curr, 0);
  return sumVal;
}

const output = positiveSum([1, -2, 3, 4, 5]);
console.log(output);