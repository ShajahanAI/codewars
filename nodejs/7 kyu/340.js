// https://www.codewars.com/kata/5aba780a6a176b029800041c/train/javascript

// Passed

function maxMultiple(divisor, bound) {
  let result;
  for (let num = divisor; num <= bound; num++) {
    if (num % divisor === 0) {
      result = num;
    }
  }

  return result;
}

const output = maxMultiple(37, 200);
console.log(output);