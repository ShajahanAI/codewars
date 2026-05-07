// https://www.codewars.com/kata/560d6ebe7a8c737c52000084/train/javascript

// Passed

function notVisibleCubes(n) {
  let result = n <= 2 ? 0 : (n - 2) ** 3;
  return result;
}

const output = notVisibleCubes(5);
console.log(output);