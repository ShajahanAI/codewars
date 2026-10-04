// https://www.codewars.com/kata/5a91a7c5fd8c061367000002/train/javascript

// Passed

function minimumSteps(numbers, value) {
  let sortedArr = numbers.sort((a, b) => a - b);
  let result = 0;
  let currentSum = 0;
  for (const num of sortedArr) {
    if (currentSum >= value) {
      break;
    }

    currentSum += num;
    result++;
  }

  result--;
  return result;
}

const output = minimumSteps([19, 98, 69, 28, 75, 45, 17, 98, 67]);
console.log(output);