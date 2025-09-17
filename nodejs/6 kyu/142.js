// https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/javascript

// Passed

function upArray(arr) {
  if (arr.length === 0 || !arr.every((num) => num < 10 && num >= 0))
    return null;

  for (let idx = arr.length - 1; idx > -1; idx--) {
    if (arr[idx] !== 9) {
      arr[idx] += 1;
      break;
    } else if (arr[idx] === 9 && idx === 0) {
      arr[idx] = 0;
      arr = [1].concat(arr);
    } else {
      arr[idx] = 0;
    }
  }

  return arr;
}

const output = upArray([0, 7]);
console.log(output);