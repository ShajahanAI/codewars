// https://www.codewars.com/kata/5a40c250c5e284a76400008c/train/javascript

// Passed

function bouncingBall(initial, proportion) {
  let currentHeight = initial;
  let result = 0;
  while (currentHeight > 1) {
    result++;
    currentHeight *= proportion;
  }

  return result;
}

const output = bouncingBall(30, 0.3);
console.log(output);