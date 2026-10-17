// https://www.codewars.com/kata/57c3eb9fd6cf0ffd68000222/train/javascript

// Passed

function solveIt(vi, vf, t) {
  let result = [];

  if (vi <= vf) {
    let roundToTwoDecimalPlaces = (val) => Math.round(val * 100) / 100;
    let acceleration = (vf - vi) / t;
    let distance = vi * t + 0.5 * acceleration * t ** 2;
    result = [acceleration, distance].map(roundToTwoDecimalPlaces);
  }
  return result;
}

const output = solveIt(12, 56, 3.55);
console.log(output);