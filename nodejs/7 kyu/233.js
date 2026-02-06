// https://www.codewars.com/kata/59bd84b8a0640e7c49002398/train/javascript

// Passed

function tArea(tStr) {
  let triangleArray = tStr.split("\n").filter((row) => row.length);
  let height = triangleArray.length - 1;
  let base = triangleArray[height - 1]
    .split("")
    .filter((char) => char === ".").length;
  let area = (1 / 2) * base * height;
  return area;
}

const output = tArea(
  "\n.\n. .\n. . .\n. . . .\n. . . . .\n. . . . . .\n. . . . . . .\n. . . . . . . .\n. . . . . . . . .\n",
);
console.log(output);