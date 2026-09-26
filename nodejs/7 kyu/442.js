// https://www.codewars.com/kata/57cc981a58da9e302a000214/train/javascript

// Passed

function smallEnough(a, limit) {
  let result = a.every((num) => num <= limit);
  return result;
}

const output = smallEnough([101, 45, 75, 105, 99, 107], 107);
console.log(output);