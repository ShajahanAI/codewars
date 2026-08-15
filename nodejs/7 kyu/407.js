// https://www.codewars.com/kata/55736129f78b30311300010f/train/javascript

// Passed

function pattern(n) {
  let rowsReversed = [];
  let row = "";
  for (let num = n; num >= 1; num--) {
    row = String(num) + row;
    rowsReversed.push(row);
  }

  let rows = rowsReversed.reverse();
  let result = rows.join("\n");
  return result;
}

const output = pattern(5);
console.log(output);