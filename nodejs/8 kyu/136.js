// https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/javascript

// Passed

function digitize(n) {
  let result = String(n)
    .split("")
    .reverse()
    .map((strNum) => Number(strNum));
  return result;
}

const output = digitize(35231);
console.log(output);