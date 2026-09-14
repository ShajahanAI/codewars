// https://www.codewars.com/kata/5503013e34137eeeaa001648/train/javascript

// Passed

function diamond(n) {
  if (n <= 0 || n % 2 === 0) {
    return null;
  }

  let upsideDownTriangleRows = [];
  let createRow = (size, rowSize) => {
    let whitespaceCount = (rowSize - size) / 2;
    let row = " ".repeat(whitespaceCount) + "*".repeat(size);
    return row;
  };
  for (let asterixCount = n; asterixCount >= 1; asterixCount -= 2) {
    let row = createRow(asterixCount, n);
    upsideDownTriangleRows.push(row);
  }

  let diamondRows = [...upsideDownTriangleRows]
    .reverse()
    .concat(upsideDownTriangleRows.slice(1, upsideDownTriangleRows.length + 1));
  let result = diamondRows.join("\n") + "\n";
  return result;
}

const output = diamond(5);
console.log(output);