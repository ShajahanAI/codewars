// https://www.codewars.com/kata/5783d8f3202c0e486c001d23/train/javascript

// Passed

function toNumberArray(stringarray) {
  let result = stringarray.map((num) => Number(num));
  return result;
}

const output = toNumberArray(["1.1", "2.2", "3.3"]);
console.log(output);