// https://www.codewars.com/kata/5893f43b779ce54da4000124/train/javascript

// Passed

function arrayChange(arr) {
  let increaseCount = 0;
  for (let idx = 0; idx < arr.length; idx++) {
    if (idx === arr.length - 1) {
      break;
    }

    if (arr[idx + 1] - arr[idx] <= 0) {
      let toIncrease = arr[idx] + 1 - arr[idx + 1];
      increaseCount += toIncrease;
      arr[idx + 1] += toIncrease;
    }
  }

  return increaseCount;
}

const output = arrayChange([1, 1, 1]);
console.log(output);