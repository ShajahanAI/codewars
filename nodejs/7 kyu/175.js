// https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/javascript

// Passed

function evenNumbers(array, number) {
  let result = [];
  for (const num of array.reverse()) {
    if (result.length === number) {
      break;
    }

    if (num % 2 === 0) {
      result.push(num);
    }
  }

  result = result.reverse();
  return result;
}

const output = evenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3);
console.log(output);