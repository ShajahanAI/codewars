// https://www.codewars.com/kata/69b83710b26939b35fd10429/train/javascript

// Passed

function shipOfTheseus(ship) {
  let rowIdx = 0;
  let firstRowLength = ship.length !== 0 ? ship[0].length : 0;
  for (const row of ship) {
    if (rowIdx === ship.length - 1) {
      // we are in the last row
      break;
    }

    let nextRow = ship[rowIdx + 1];
    if (row.length !== firstRowLength || nextRow.length !== firstRowLength) {
      return false;
    }

    let elementsChanged = 0;
    for (let idx = 0; idx < row.length; idx++) {
      if (row[idx] !== nextRow[idx]) {
        elementsChanged++;
      }

      if (elementsChanged > 1) {
        return false;
      }
    }

    if (elementsChanged === 0) {
      return false;
    }

    rowIdx++;
  }

  return true;
}

const output = shipOfTheseus([
  ["a", "b", "c"],
  ["x", "b", "c"],
  ["x", "y", "c"],
  ["x", "y", "z"],
]);
console.log(output);