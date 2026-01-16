// https://www.codewars.com/kata/57faa6ff9610ce181b000028/train/javascript

// Passed

function crap(x, bags, cap) {
  let crapCount = 0;
  for (let row of x) {
    for (let item of row) {
      if (item === "@") {
        crapCount++;
      } else if (item === "D") {
        return "Dog!!";
      }
    }
  }

  let result = crapCount > bags * cap ? "Cr@p" : "Clean";
  return result;
}

const output = crap(
  [
    ["_", "_", "_", "_"],
    ["_", "_", "_", "@"],
    ["_", "_", "@", "_"],
  ],
  2,
  2
);
console.log(output);