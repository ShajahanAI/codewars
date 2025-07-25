// https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/javascript

// Passed

function invert(array) {
  let invertedArray = array.map((num) => -num);
  return invertedArray;
}

const output = invert([1, 2, 3, 4, 5]);
console.log(output);