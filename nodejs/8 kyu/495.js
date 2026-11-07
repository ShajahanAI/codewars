// https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/javascript

// Passed

function findMultiples(integer, limit) {
  let result = [];
  for (let num = integer; num <= limit; num += integer) {
    result.push(num);
  }

  return result;
}

const output = findMultiples(5, 25);
console.log(output);