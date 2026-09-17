// https://www.codewars.com/kata/64b8c6c09416795eb9fbdcbf/train/javascript

// Passed

function repSet(n) {
  if (n === 0) {
    return [];
  }

  let result = [];
  for (let currentNum = 0; currentNum < n; currentNum++) {
    let currentNumSet = repSet(currentNum);
    result.push(currentNumSet);
  }

  return result;
}

const output = repSet(3);
console.log(output);