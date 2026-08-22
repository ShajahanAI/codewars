// https://www.codewars.com/kata/5e4e8f5a72d9550032953717/train/javascript

// Passed

function* allRationals() {
  let baseFractions = [[1, 1]];
  yield baseFractions[0];

  while (true) {
    let nextBaseFractions = [];
    for (const baseFraction of baseFractions) {
      let [numerator, denominator] = baseFraction;
      let [fraction1, fraction2] = [
        [numerator, denominator + numerator],
        [numerator + denominator, denominator],
      ];
      nextBaseFractions.push(fraction1);
      nextBaseFractions.push(fraction2);

      yield fraction1;
      yield fraction2;
    }

    baseFractions = nextBaseFractions;
  }
}

const output = allRationals().next();
console.log(output);