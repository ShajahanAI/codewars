// https://www.codewars.com/kata/563e320cee5dddcf77000158/train/javascript

// Passed

function getAverage(marks) {
  let result = Math.floor(
    marks.reduce((prev, curr) => prev + curr, 0) / marks.length,
  );
  return result;
}

const output = getAverage([1, 1, 1, 1, 1, 1, 1, 2]);
console.log(output);