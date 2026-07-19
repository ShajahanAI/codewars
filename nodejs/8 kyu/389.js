// https://www.codewars.com/kata/55685cd7ad70877c23000102/train/javascript

// Passed

function makeNegative(num) {
  let negativeNumber = num > 0 ? num * -1 : num;
  return negativeNumber;
}

const output = makeNegative(42);
console.log(output);