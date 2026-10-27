// https://www.codewars.com/kata/58f625e20290fb29c3000056/train/javascript

// Passed

function alternate(items) {
  let result = items.length ? !items.every((item) => item === false) : null;
  return result;
}

const output = alternate([true, false, true]);
console.log(output);