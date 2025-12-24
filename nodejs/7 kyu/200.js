// https://www.codewars.com/kata/54fdfe14762e2edf4a000a33/train/javascript

// Passed

function fire(x, y) {
  let battleField = [
    "top left",
    "top middle",
    "top right",
    "middle left",
    "center",
    "middle right",
    "bottom left",
    "bottom middle",
    "bottom right",
  ];
  let monoIndex = y * 3 + x;
  let sector = battleField[monoIndex];
  return sector;
}

const output = fire(1, 2);
console.log(output);