// https://www.codewars.com/kata/589b1c15081bcbfe6700017a/train/javascript

// Passed

function cost(mins) {
  let totalCharges = 30;
  if (mins <= 60) {
    return totalCharges;
  }

  let numberOfClassesTaken = Math.floor(mins / 30) - 1;
  if (mins % 30 <= 5) {
    numberOfClassesTaken -= 1;
  }

  totalCharges += numberOfClassesTaken * 10;
  return totalCharges;
}

const output = cost(273);
console.log(output);