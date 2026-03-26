// https://www.codewars.com/kata/602db3215c22df000e8544f0/train/javascript

// Passed

function twoArePositive(a, b, c) {
  let positiveCount = 0;
  nums = [a, b, c];
  for (const num of nums) {
    if (num > 0) {
      positiveCount++;
    }
  }

  let result = positiveCount === 2;
  return result;
}

const output = twoArePositive(2, 4, -3);
console.log(output);