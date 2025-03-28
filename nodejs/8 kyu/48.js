// https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/javascript

// Passed

function removeEveryOther(arr) {
  return arr.filter((val, idx) => idx % 2 === 0);
}

const output = removeEveryOther(['Hello', 'Goodbye', 'Hello Again']);
console.log(output);