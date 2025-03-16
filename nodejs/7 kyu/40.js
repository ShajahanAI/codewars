// https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2/train/javascript

// Passed

function solution(pairs) {
  const humanReadableString = Object.entries(pairs)
    .map((entry) => `${entry[0]} = ${entry[1]}`)
    .join(",");
  return humanReadableString;
}

const output = solution({ a: "b", b: "a" });
console.log(output);