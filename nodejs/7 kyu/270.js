// https://www.codewars.com/kata/5546180ca783b6d2d5000062/train/javascript

// Passed

function squares(x, n) {
  let result = [];
  for (let i = 0; i < n; i++) {
    let elem = x ** (2 ** i);
    result.push(elem);
  }

  return result;
}

const output = squares(2, 5);
console.log(output);