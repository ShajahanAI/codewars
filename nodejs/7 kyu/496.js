// https://www.codewars.com/kata/5520714decb43308ea000083/train/javascript

// Passed

function root(x, n) {
  let result = Math.pow(x, 1 / n);
  return result;
}

const output = root(6.25, 2);
console.log(output);