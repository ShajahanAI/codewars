// https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/javascript

// Passed

function removeSmallest(numbers) {
  let minIdx = 0;
  for (let idx = 0; idx < numbers.length; idx++) {
    if (numbers[idx] < numbers[minIdx]) {
      minIdx = idx;
    }
  }

  let result = numbers.slice(0, minIdx).concat(numbers.slice(minIdx + 1));
  return result;
}

const output = removeSmallest([2, 2, 1, 2, 1]);
console.log(output);