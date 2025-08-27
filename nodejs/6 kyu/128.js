// https://www.codewars.com/kata/559e708e72d342b0c900007b/train/javascript

// Passed

function EvenOdd(arr) {
  const result = arr.reduce((prev, curr, idx) =>
    idx % 2 === 1 ? prev * curr : prev + curr
  );
  return result;
}

const output = EvenOdd([1, 2, 2, 1, 6, 1, 3, 9, 6, 1]);
console.log(output);