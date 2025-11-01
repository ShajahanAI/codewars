// https://www.codewars.com/kata/596f6385e7cd727fff0000d6/train/javascript

// Passed

function avgArray(arr) {
  let averages = [];
  for (idx = 0; idx < arr[0].length; idx++) {
    let idxSum = 0;
    for (valArr of arr) {
      idxSum += valArr[idx];
    }
    let average = idxSum / arr.length;
    averages.push(average);
  }

  return averages;
}

const output = avgArray([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
]);
console.log(output);