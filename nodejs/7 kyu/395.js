// https://www.codewars.com/kata/5a036ecb2b651d696f00007c/train/javascript

// Passed

function drawACross(n) {
  let result;
  if (n < 3) {
    result = "Not possible to draw cross for grids less than 3x3!";
  } else {
    let rows = [];
    let isCenteredCrossPossible = false;
    for (let rowIdx = 0; rowIdx < n; rowIdx++) {
      let row = " ".repeat(n).split("");
      let [startIdx, endIdx] = [rowIdx, n - rowIdx - 1];
      row[startIdx] = "x";
      row[endIdx] = "x";
      if (startIdx === endIdx) {
        isCenteredCrossPossible = true;
      }
      rows.push(row);
    }

    result = "Centered cross not possible!";
    if (isCenteredCrossPossible) {
      rows = rows.map((row) => row.join(""));
      result = rows.join("\n");
    }
  }

  return result;
}

const output = drawACross(7);
console.log(output);