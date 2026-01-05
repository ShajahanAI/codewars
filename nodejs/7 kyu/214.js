// https://www.codewars.com/kata/5806445c3f1f9c2f72000031/train/javascript

// Passed

function meanVsMedian(numbers) {
  numbers = numbers.sort((a, b) => a - b);
  let mean = numbers.reduce((prev, curr) => prev + curr, 0) / numbers.length;
  let idx, median;
  if (numbers.length % 2 === 0) {
    idx = numbers.length / 2;
    median = (numbers[idx] + numbers[idx + 1]) / 2;
  } else {
    idx = Math.floor(numbers.length / 2);
    median = numbers[idx];
  }

  if (mean > median) {
    return "mean";
  } else if (median > mean) {
    return "median";
  } else {
    return "same";
  }
}

const output = meanVsMedian([1, 2, 37]);
console.log(output);