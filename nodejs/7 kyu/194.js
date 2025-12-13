// https://www.codewars.com/kata/56d02e6cc6c8b49c510005bb/train/javascript

// Passed

function findMissingNumbers(arr) {
  let missingNumbers = [];
  for (let idx = 0; idx < arr.length; idx++) {
    if (idx === arr.length - 1) {
      break;
    }

    if (arr[idx + 1] - arr[idx] === 1) {
      continue;
    }

    for (let num = arr[idx] + 1; num < arr[idx + 1]; num++) {
      missingNumbers.push(num);
    }
  }

  return missingNumbers;
}

const output = findMissingNumbers([-3, -2, 1, 4]);
console.log(output);