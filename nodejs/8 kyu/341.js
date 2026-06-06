// https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/javascript

// Passed

function twoHighest(arr) {
  arr = Array.from(new Set(arr.sort((a, b) => a - b)));
  let result = [];
  if (arr.length !== 0) {
    result =
      arr.length >= 2 && arr[arr.length - 1] !== arr[0]
        ? [arr[arr.length - 1], arr[arr.length - 2]]
        : [arr[0]];
  }

  return result;
}

const output = twoHighest([15, 20, 20, 17]);
console.log(output);