// https://www.codewars.com/kata/578fdcfc75ffd1112c0001a1/train/javascript

// Passed

function binRota(arr) {
  let binRotationPlan = [];
  let rowIdx = 0;
  for (const row of arr) {
    if (rowIdx % 2 === 0) {
      binRotationPlan = binRotationPlan.concat(row);
    } else {
      binRotationPlan = binRotationPlan.concat(row.reverse());
    }

    rowIdx++;
  }

  return binRotationPlan;
}

const output = binRota([
  ["Bob", "Nora"],
  ["Ruby", "Carl"],
]);
console.log(output);