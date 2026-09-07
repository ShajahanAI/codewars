// https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/javascript

// Passed

function gimme(triplet) {
  let numberToIdxMap = new Object();
  for (let idx = 0; idx < triplet.length; idx++) {
    let number = triplet[idx];
    numberToIdxMap[number] = idx;
  }

  triplet = triplet.sort((a, b) => a - b);
  let middleNumber = triplet[1];
  let result = numberToIdxMap[middleNumber];
  return result;
}

const output = gimme([2, 3, 1]);
console.log(output);