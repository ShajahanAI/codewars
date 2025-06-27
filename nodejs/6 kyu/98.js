// https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/javascript

// Passed

function looseChange(cents) {
  const changeMap = { Nickels: 0, Pennies: 0, Dimes: 0, Quarters: 0 };
  if (cents <= 0) return changeMap;

  cents = Math.floor(cents);
  const centToChangeMap = {
    25: "Quarters",
    10: "Dimes",
    5: "Nickels",
    1: "Pennies",
  };

  for (const changeValue of [25, 10, 5, 1]) {
    let changeCount = Math.floor(cents / changeValue);
    if (changeCount < 1) continue;

    // change can hold part of total cents
    change = centToChangeMap[changeValue];
    changeMap[change] += changeCount;
    cents -= Math.floor(cents / changeValue) * changeValue;
  }

  return changeMap;
}

const output = looseChange(56);
console.log(output);