// https://www.codewars.com/kata/57e1857d333d8e0f76002169/train/javascript

// Passed

const CHANGE = {
  penny: 0.01,
  nickel: 0.05,
  dime: 0.4,
  quarter: 0.25,
  dollar: 1,
};

function changeCount(change) {
  const numericalValue = change
    .toLowerCase()
    .split(" ")
    .map((c) => CHANGE[c]);
  const totalValue = numericalValue.reduce((prev, curr) => prev + curr, 0);
  return '$' + totalValue.toFixed(2);
}

const output = changeCount('dime penny dollar');
console.log(output);