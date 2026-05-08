// https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/javascript

// Passed

function closeCompare(a, b, margin = 0) {
  let absoluteDistance = Math.abs(a - b);
  let result;
  if (absoluteDistance <= margin) {
    result = 0;
  } else {
    result = a > b ? 1 : -1;
  }

  return result;
}

const output = closeCompare(2, 5, 3);
console.log(output);