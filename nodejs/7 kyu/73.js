// https://www.codewars.com/kata/5727868888095bdf5c001d3d/train/javascript

// Passed

function stringToIntArray(s) {
  const numberArray = s
    .split(",")
    .map((number) => (number !== "" ? Number(number) : null))
    .filter((number) => number !== null);
  return numberArray;
}

const output = stringToIntArray("21,12,23,34,45");
console.log(output);