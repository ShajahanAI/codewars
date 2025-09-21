// https://www.codewars.com/kata/5a34f087c5e28462d9000082/train/javascript

// Passed

function swapHeadAndTail(arr) {
  let middleIdxToSlice = Math.floor(arr.length / 2);
  let swappedArr;
  if (arr.length % 2 === 0) {
    swappedArr = arr
      .slice(middleIdxToSlice)
      .concat(arr.slice(0, middleIdxToSlice));
  } else {
    swappedArr = arr
      .slice(middleIdxToSlice + 1)
      .concat([arr[middleIdxToSlice], ...arr.slice(0, middleIdxToSlice)]);
  }

  return swappedArr;
}

const output = swapHeadAndTail([1, 2, -3, 4, 5, 6, -7, 8]);
console.log(output);