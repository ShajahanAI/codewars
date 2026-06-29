// https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/javascript

// Passed

function findSmallestInt(arr) {
  let result = Math.min(...arr);
  return result;
}

const output = findSmallestInt([78, 56, 232, 12, 8]);
console.log(output);