// https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/javascript

// Passed

function findOutlier(integers) {
  let evenAndOddCount = [0, 0];
  let isOutlierEven;
  for (const num of integers) {
    let absNum = Math.abs(num);
    evenAndOddCount[absNum % 2]++;

    let [evenCount, oddCount] = evenAndOddCount;
    if (evenCount > 1) {
      isOutlierEven = false;
      break;
    } else if (oddCount > 1) {
      isOutlierEven = true;
      break;
    }
  }

  let outlier = isOutlierEven
    ? integers.find((elem) => Math.abs(elem) % 2 === 0)
    : integers.find((elem) => Math.abs(elem) % 2 === 1);
  return outlier;
}

const output = findOutlier([2, 6, 8, 10, 3]);
console.log(output);