// https://www.codewars.com/kata/559e10e2e162b69f750000b4/train/javascript

// Passed

function dominator(arr) {
  let valueToCountMap = new Object();
  for (const num of arr) {
    if (!(num in valueToCountMap)) {
      valueToCountMap[num] = 0;
    }

    valueToCountMap[num]++;
  }

  let result = -1;
  let lengthToCompare = Math.floor(arr.length / 2);
  for (const num of Object.keys(valueToCountMap)) {
    if (valueToCountMap[num] > lengthToCompare) {
      result = Number(num);
      break;
    }
  }

  return result;
}

const output = dominator([3, 4, 3, 2, 3, 1, 3, 3]);
console.log(output);