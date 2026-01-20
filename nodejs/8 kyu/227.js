// https://www.codewars.com/kata/5b4e779c578c6a898e0005c5/train/javascript

// Passed

function drawStairs(n) {
  let rows = [];
  for (let rowCount = 1; rowCount <= n; rowCount++) {
    let row = " ".repeat(rowCount - 1) + "I";
    rows.push(row);
  }

  let stairs = rows.join("\n");
  return stairs;
}

const output = drawStairs(5);
console.log(output);