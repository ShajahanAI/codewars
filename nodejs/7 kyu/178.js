// https://www.codewars.com/kata/5937ae46377144bb2f000029/train/javascript

// Passed

function getRectangleString(width, height) {
  let rows = [];
  for (let rowCount = 1; rowCount <= height; rowCount++) {
    let row;
    if (rowCount === 1 || rowCount === height) {
      row = "*".repeat(width);
    } else {
      row = width === 1 ? "*" : "*" + " ".repeat(width - 2) + "*";
    }

    rows.push(row);
  }

  let rectangle = rows.join("\r\n") + "\r\n";
  return rectangle;
}

const output = getRectangleString(5, 7);
console.log(output);