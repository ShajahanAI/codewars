// https://www.codewars.com/kata/65127141a5de2b1dcb40927e/train/javascript

// Passed

function spinAround(turns) {
  let turnValues = turns.map((turn) => (turn === "right" ? 90 : -90));
  let absTurnInDegrees = Math.abs(
    turnValues.reduce((prev, curr) => prev + curr, 0),
  );
  let result = Math.floor(absTurnInDegrees / 360);
  return result;
}

const output = spinAround([
  "right",
  "right",
  "right",
  "left",
  "right",
  "right",
]);
console.log(output);