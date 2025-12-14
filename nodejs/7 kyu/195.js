// https://www.codewars.com/kata/563d54a7329a7af8f4000059/train/javascript

// Passed

function buildRowText(index, character) {
  let rowArr = [];
  for (let idx = 0; idx < 10; idx++) {
    rowArr.push("|");
  }
  let row = rowArr.join(" ");
  let rowWithCharacter =
    row.slice(0, index * 2 + 1) + character + row.slice(index * 2 + 2);
  return rowWithCharacter;
}

const output = buildRowText(2, "A");
console.log(output);