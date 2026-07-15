// https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/javascript

// Passed

function inAscOrder(arr) {
  let result = arr.every(
    (elem, idx) => idx === arr.length - 1 || elem <= arr[idx + 1],
  );
  return result;
}

const output = inAscOrder([1, 2, 4, 7, 19]);
console.log(output);