// https://www.codewars.com/kata/545991b4cbae2a5fda000158/train/javascript

// Passed

function include(arr, item) {
  let result = arr.includes(item);
  return result;
}

const output = include([1, 2, 3, 4], 3);
console.log(output);