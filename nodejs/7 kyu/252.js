// https://www.codewars.com/kata/57d2807295497e652b000139/train/javascript

// Passed

function averages(numbers) {
  let averagesArr = [];
  if (numbers === null || [1, 0].includes(numbers.length)) {
    return averagesArr;
  }

  for (let idx = 0; idx < numbers.length - 1; idx++) {
    let average = (numbers[idx] + numbers[idx + 1]) / 2;
    averagesArr.push(average);
  }

  return averagesArr;
}

const output = averages([1, 3, 5, 1, -10]);
console.log(output);