// https://www.codewars.com/kata/5884615cbd573356ab000050/train/javascript

// Passed

function countSumOfTwoRepresentations(n, l, r) {
  let result = 0;
  let seen = new Set();
  for (let num = l; num <= r; num++) {
    let numToAdd = n - num;

    if (seen.has(num)) {
      continue;
    }

    if (numToAdd >= l && numToAdd <= r) {
      result++;
      seen.add(numToAdd);
    }
  }

  return result;
}

const output = countSumOfTwoRepresentations(6, 2, 4);
console.log(output);