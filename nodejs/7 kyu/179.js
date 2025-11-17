// https://www.codewars.com/kata/5631213916d70a0979000066/train/javascript

// Passed

function pattern(n) {
  let rows = [];
  for (let rowCount = 1; rowCount <= n; rowCount++) {
    let row =
      rowCount === 1 ? "1" : "1" + "*".repeat(rowCount - 1) + String(rowCount);
    rows.push(row);
  }

  let result = rows.join("\n");
  return result;
}

const output = pattern(20);
console.log(output);