// https://www.codewars.com/kata/571965ccdf7fdb10a00000ea/train/javascript

// Passed

function sumLength(array) {
  let [totalSum, negativeCount] = [0, 0];
  let isNegativeZero = true;
  for (const num of array) {
    if (num > 0) {
      totalSum += num;
    } else {
      if (num === 0) {
        if (!isNegativeZero) {
          isNegativeZero = true; // next 0 is going to be negative
          continue; // skipping this 0 as it it not negative
        }

        isNegativeZero = false;
      }

      negativeCount++;
    }
  }

  let result = `${totalSum} ${negativeCount}`;
  return result;
}

const output = sumLength([-1, 2, 3, 4, 0, 1, 0, -2, 0, -3]);
console.log(output);