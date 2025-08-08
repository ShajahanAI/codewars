// https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/javascript

// Passed

function countRedBeads(n) {
  if (n < 2) return 0;
  return (n - 1) * 2;
}

const output = countRedBeads(5);
console.log(output);