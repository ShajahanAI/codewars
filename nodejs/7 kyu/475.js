// https://www.codewars.com/kata/55749101ae1cf7673800003e/train/javascript

// Passed

function pattern(n) {
  let rows = [];
  let totalRows = n % 2 === 1 ? (n - 1) / 2 : n / 2;
  let currentNum = 2;
  for (let rowNum = 1; rowNum <= totalRows; rowNum++) {
    let row = String(currentNum).repeat(rowNum * 2);
    rows.push(row);
    currentNum += 2;
  }

  let result = rows.join("\n");
  return result;
}

const output = pattern(5);
console.log(output);