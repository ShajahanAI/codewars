// https://www.codewars.com/kata/558aa460dcfb4a94c40001d7/train/javascript

// Passed

const [GALLON_TO_LITER, MILE_TO_KILOMETER] = [3.785411784, 1.609344];
const [LITER_TO_GALLON, KILOMETER_TO_MILE] = [
  1 / GALLON_TO_LITER,
  1 / MILE_TO_KILOMETER,
];

function roundToTwoDecimalPlaces(num) {
  let result = Math.round(num * 100) / 100;
  return result;
}

function mpg2lp100km(x) {
  let result = 100 / (x * (MILE_TO_KILOMETER / GALLON_TO_LITER));
  result = roundToTwoDecimalPlaces(result);
  return result;
}

function lp100km2mpg(x) {
  let result = (1 / (x * (LITER_TO_GALLON / KILOMETER_TO_MILE))) * 100;
  result = roundToTwoDecimalPlaces(result);
  return result;
}

const output1 = mpg2lp100km(42);
const output2 = lp100km2mpg(9);
console.log(output1, output2);