// https://www.codewars.com/kata/5a996f3d5084d73a7100040c/train/javascript

// Passed

function deathStar(week) {
  let lastDayIdx = week[week.length - 1];

  let [iron, steel, chromium] = [0, 0, 0];
  for (let idx = 0; idx < lastDayIdx; idx++) {
    let quantities = week[idx];
    iron += quantities[0];
    steel += quantities[1];
    chromium += quantities[2];
  }

  let result;
  if (iron >= 100 && steel >= 75 && chromium >= 50) {
    result = "The station is completed!";
  } else {
    let calculateRequired = (quantityRequired, availableQuantity) =>
      Math.max(quantityRequired - availableQuantity, 0);
    let ironRequired = calculateRequired(100, iron);
    let steelRequired = calculateRequired(75, steel);
    let chromiumRequired = calculateRequired(50, chromium);
    result = `The station is destroyed! It needed ${ironRequired} iron, ${steelRequired} steel and ${chromiumRequired} chromium for completion.`;
  }

  return result;
}

const output = deathStar([
  [100, 75, 49],
  [20, 15, 20],
  [10, 15, 10],
  [50, 50, 20],
  [20, 15, 10],
  [20, 15, 10],
  [20, 15, 10],
  1,
]);
console.log(output);