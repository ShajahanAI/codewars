// https://www.codewars.com/kata/5d376cdc9bcee7001fcb84c0/train/javascript

// Passed

function oddOnesOut(nums) {
  let numToCountMap = new Object();

  for (const num of nums) {
    if (!(num in numToCountMap)) {
      numToCountMap[num] = 0;
    }

    numToCountMap[num]++;
  }

  let result = nums.filter((num) => numToCountMap[num] % 2 === 0);
  return result;
}

const output = oddOnesOut([
  82, 86, 71, 58, 44, 79, 50, 44, 79, 67, 82, 82, 55, 50,
]);
console.log(output);