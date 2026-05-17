// https://www.codewars.com/kata/555b73a81a6285b6ce000047/train/javascript

// Passed

function add(...args) {
  let multiplier = 1;
  let result = 0;
  for (const num of args) {
    result += multiplier * num;
    multiplier++;
  }

  return result;
}

const output = add(100, 200, 300);
console.log(output);