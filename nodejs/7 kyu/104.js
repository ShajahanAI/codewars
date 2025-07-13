// https://www.codewars.com/kata/56b1eb19247c01493a000065/train/javascript

// Passed

function uniqueSum(lst) {
  let uniqueNums = [];
  for (const num of lst) {
    if (uniqueNums.includes(num)) continue;
    uniqueNums.push(num);
  }

  const result = uniqueNums.reduce((prev, curr) => prev + curr, null);
  return result;
}

const output = uniqueSum([1,3,8,1,8]);
console.log(output);