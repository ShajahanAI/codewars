// https://www.codewars.com/kata/5a043724ffe75fbab000009f/train/javascript

// Passed

function reverseMiddle(array) {
  let isEven = array.length % 2 === 0;
  let startIdx = Math.floor(array.length / 2) - 1;
  let result = array
    .slice(startIdx, isEven ? startIdx + 2 : startIdx + 3)
    .reverse();
  return result;
}

const output = reverseMiddle([1, 2, 3, 4, 5, 6]);
console.log(output);