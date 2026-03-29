// https://www.codewars.com/kata/56b97b776ffcea598a0006f2/train/javascript

// Passed

function bubblesortOnce(a) {
  let arr = [...a];
  for (let idx = 0; idx < arr.length - 1; idx++) {
    if (arr[idx] > arr[idx + 1]) {
      [arr[idx], arr[idx + 1]] = [arr[idx + 1], arr[idx]];
    }
  }

  return arr;
}

const output = bubblesortOnce([9, 7, 5, 3, 1, 2, 4, 6, 8]);
console.log(output);