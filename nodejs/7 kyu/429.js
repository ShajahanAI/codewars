// https://www.codewars.com/kata/5c4cb8fc3cf185147a5bdd02/train/javascript

// Passed

function sumOrProduct(array, n) {
  array = array.sort((a, b) => a - b);
  let sum = array
    .slice(array.length - n)
    .reduce((prev, curr) => prev + curr, 0);
  let product = array.slice(0, n).reduce((prev, curr) => prev * curr, 1);

  let result;
  if (sum > product) {
    result = "sum";
  } else if (product > sum) {
    result = "product";
  } else {
    result = "same";
  }

  return result;
}

const output = sumOrProduct([10, 41, 8, 16, 20, 36, 9, 13, 20], 3);
console.log(output);