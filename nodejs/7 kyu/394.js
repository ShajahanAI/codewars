// https://www.codewars.com/kata/576a29ab726f4bba4b000bb1/train/javascript

// Passed

function nameScore(name) {
  let groups = ["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY"];
  let letterToScoreMap = new Object();
  for (let idx = 0; idx < groups.length; idx++) {
    let group = groups[idx];
    let score = idx + 1;
    for (const letter of group) {
      letterToScoreMap[letter] = score;
    }
  }

  let totalScore = 0;
  for (const char of name.toUpperCase()) {
    if (char in letterToScoreMap) {
      totalScore += letterToScoreMap[char];
    }
  }

  let result = new Object();
  result[name] = totalScore;
  return result;
}

const output = nameScore("Mary Jane");
console.log(output);