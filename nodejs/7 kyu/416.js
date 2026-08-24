// https://www.codewars.com/kata/5dd259444228280032b1ed2a/train/javascript

// Passed

function solve(s, g) {
  let result = -1;
  for (let num1 = g; num1 <= Math.ceil(s / 2); num1 += g) {
    let num2 = s - num1;
    if (num2 % g === 0) {
      result = [num1, num2];
      break;
    }
  }

  return result;
}

const output = solve(12, 4);
console.log(output);