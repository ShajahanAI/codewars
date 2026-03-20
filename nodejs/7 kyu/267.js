// https://www.codewars.com/kata/5663f5305102699bad000056/train/javascript

// Passed

function mxdiflg(a1, a2) {
  if (a1.length === 0 || a2.length === 0) {
    return -1;
  }

  let computeLengths = (arr) => arr.map((word) => word.length);
  let [a1Lengths, a2Lengths] = [computeLengths(a1), computeLengths(a2)];

  let [a1Max, a1Min, a2Max, a2Min] = [
    Math.max(...a1Lengths),
    Math.min(...a1Lengths),
    Math.max(...a2Lengths),
    Math.min(...a2Lengths),
  ];

  let possibleCombinations = [
    Math.abs(a1Max - a2Min),
    Math.abs(a1Min - a2Min),
    Math.abs(a1Max - a2Max),
    Math.abs(a2Max - a1Min),
  ];

  let result = Math.max(...possibleCombinations);
  return result;
}

const output = mxdiflg(
  [
    "hoqq",
    "bbllkw",
    "oox",
    "ejjuyyy",
    "plmiis",
    "xxxzgpsssa",
    "xxwwkktt",
    "znnnnfqknaz",
    "qqquuhii",
    "dvvvwz",
  ],
  ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"],
);
console.log(output);