// https://www.codewars.com/kata/5a651865fd56cb55760000e0/train/javascript

// Passed

function arrayLeaders(numbers) {
  let arrSum = numbers.reduce((prev, curr) => prev + curr, 0);
  let result = [];
  for (const num of numbers) {
    arrSum -= num;
    if (num > arrSum) {
      result.push(num);
    }
  }

  return result;
}

const output = arrayLeaders([16, 17, 4, 3, 5, 2]);
console.log(output);