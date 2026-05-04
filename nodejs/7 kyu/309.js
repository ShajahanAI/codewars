// https://www.codewars.com/kata/59b44d00bf10a439dd00006f/train/javascript

// Passed

function add(arr) {
  let result = [];
  let sum = 0;
  for (const num of arr) {
    sum += num;
    result.push(sum);
  }

  return result;
}

const output = add([1, 2, 3, 4, 5]);
console.log(output);