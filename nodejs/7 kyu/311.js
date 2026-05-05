// https://www.codewars.com/kata/62a611067274990047f431a8/train/javascript

// Passed

function alternate(n, firstValue, secondValue) {
  let result = [];
  let values = [firstValue, secondValue];
  for (let i = 0; i < n; i++) {
    result.push(values[i % 2]);
  }

  return result;
}

const output = alternate(20, "blue", "red");
console.log(output);