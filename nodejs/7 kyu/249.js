// https://www.codewars.com/kata/5886d35d4703f125a6000008/train/javascript

// Passed

function isSmooth(arr) {
  if (arr[0] !== arr[arr.length - 1]) {
    return false;
  }

  let middle;
  if (arr.length % 2 === 0) {
    middle = arr[arr.length / 2 - 1] + arr[arr.length / 2];
  } else {
    middle = arr[Math.floor(arr.length / 2)];
  }

  if (arr[0] !== middle) {
    return false;
  }

  return true;
}

const output = isSmooth([-12, 34, 40, -5, -12, 4, 0, 0, -12]);
console.log(output);