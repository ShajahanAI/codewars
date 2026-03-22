// https://www.codewars.com/kata/580755730b5a77650500010c/train/javascript

// Passed

function sortMyString(S) {
  let idxedStrings = [String(), String()];
  for (let idx = 0; idx < S.length; idx++) {
    idxedStrings[idx % 2] += S[idx];
  }

  let [evenIdxedString, oddIdxedString] = idxedStrings;
  let result = `${evenIdxedString} ${oddIdxedString}`;
  return result;
}

const output = sortMyString("CodeWars");
console.log(output);