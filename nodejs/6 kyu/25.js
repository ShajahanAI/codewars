// https://www.codewars.com/kata/5208f99aee097e6552000148/train/javascript

// Passed

function solution(string) {
  const upperCaseIndices = [0].concat(
    string
      .split("")
      .map((char, index) => (char === char.toUpperCase() ? index : ""))
      .filter((value) => value !== "")
      .concat(string.length)
  );

  const words = upperCaseIndices.map((upperIndex, index) =>
    index !== upperCaseIndices.length - 1
      ? string.slice(upperIndex, upperCaseIndices[index + 1])
      : ""
  );

  return words.join(" ").trim();
}

const output = solution("camelCase");
console.log(output);
