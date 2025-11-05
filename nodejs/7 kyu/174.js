// https://www.codewars.com/kata/56242b89689c35449b000059/train/javascript

// Passed

function chessBoard(rows, columns) {
  let result = [];
  for (let rowIdx = 0; rowIdx < rows; rowIdx++) {
    let row = [];
    let isWhiteSquare = rowIdx % 2 === 0;
    for (let columnIdx = 0; columnIdx < columns; columnIdx++) {
      let square = isWhiteSquare ? "O" : "X";
      row.push(square);
      isWhiteSquare = !isWhiteSquare;
    }

    result.push(row);
  }

  return result;
}

const output = chessBoard(6, 4);
console.log(output);