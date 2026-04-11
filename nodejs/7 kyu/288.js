// https://www.codewars.com/kata/57f609022f4d534f05000024/train/javascript

// Passed

function stray(numbers) {
  let numToCountMap = new Object();

  for (const num of numbers) {
    if (!(num in numToCountMap)) {
      numToCountMap[num] = 0;
    }

    numToCountMap[num]++;
  }

  for (const num in numToCountMap) {
    if (numToCountMap[num] === 1) {
      let result = Number(num);
      return result;
    }
  }
}

const output = stray([1, 1, 2]);
console.log(output);