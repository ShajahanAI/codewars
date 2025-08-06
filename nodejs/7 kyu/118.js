// https://www.codewars.com/kata/55563df50dda59adf900004d/train/javascript

// Passed

function validateEAN(eanCode) {
  let checksum = Number(eanCode[eanCode.length - 1]);
  let sumOfOperations = eanCode
    .slice(0, eanCode.length - 1)
    .split("")
    .map((stringDigit, idx) => Number(stringDigit) * (idx % 2 === 0 ? 1 : 3))
    .reduce((prev, curr) => prev + curr);
  let calculatedChecksum =
    sumOfOperations % 10 === 0 ? 0 : 10 - (sumOfOperations % 10);
  return checksum === calculatedChecksum;
}

const output = validateEAN("9783815820865");
console.log(output);