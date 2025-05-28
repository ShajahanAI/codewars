// https://www.codewars.com/kata/5809b62808ad92e31b000031/train/javascript

// Passed

function calculate(str) {
  numbers = str
    .replaceAll("minus", "plus-")
    .split("plus")
    .map((stringNumber) => Number(stringNumber));
  const finalSum = numbers.reduce((prev, curr) => prev + curr, 0);
  return String(finalSum);
}

const output = calculate("1plus2plus3minus4");
console.log(output);