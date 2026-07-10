// https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/javascript

// Passed

function missingValues(arr) {
  let numToCountObj = new Object();
  for (const num of arr) {
    if (!(num in numToCountObj)) {
      numToCountObj[num] = 0;
    }

    numToCountObj[num]++;
  }

  let x, y;
  for (const num of Object.keys(numToCountObj)) {
    let count = numToCountObj[num];
    if (count === 1) {
      x = num;
    } else if (count === 2) {
      y = num;
    }
  }

  let result = x * x * y;
  return result;
}

const output = missingValues([1, 1, 1, 2, 2, 3]);
console.log(output);