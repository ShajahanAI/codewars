// https://www.codewars.com/kata/58afb7cea9c97a83a50000e3/train/javascript

// Passed

function fantasticPerson(table) {
  let result = -1;
  for (let personIdx = 0; personIdx < table.length; personIdx++) {
    if (table[personIdx][personIdx] === false) {
      // person doesn't identify with himself
      continue;
    }

    for (let rowIdx = 0; rowIdx < table.length; rowIdx++) {
      if (rowIdx === personIdx) {
        // we've confirmed that person identifies with himself
        continue;
      }

      if (table[rowIdx][personIdx] === true) {
        // person also identifies with someone else
        result = -1;
        break;
      } else {
        result = personIdx;
      }
    }

    if (result !== -1) {
      break;
    }
  }

  return result;
}

const output = fantasticPerson([
  [true, true, true],
  [false, true, true],
  [false, false, true],
]);
console.log(output);