// https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/javascript

// Passed

function stringy(size) {
  let result = "";
  for (let idx = 0; idx < size; idx++) {
    result += Number(idx % 2 === 0);
  }

  return result;
}

const output = stringy(3);
console.log(output);