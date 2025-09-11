// https://www.codewars.com/kata/59f70440bee845599c000085/train/javascript

// Passed

function findHack(arr) {
  let hackedNames = [];
  let isScoreHacked = (score, grades) => {
    if (score > 200) return true;

    const gradeScoreMap = {
      A: 30,
      B: 20,
      C: 10,
      D: 5,
    };

    let totalScore = grades.reduce(
      (prev, curr) => (gradeScoreMap[curr] ? prev + gradeScoreMap[curr] : prev),
      0
    );
    let addAdditionalTwentyPoints =
      grades.length >= 5 && grades.every((grade) => ["A", "B"].includes(grade));

    if (addAdditionalTwentyPoints) {
      totalScore += 20;
    }

    return totalScore !== score;
  };

  for (const studentRecord of arr) {
    if (isScoreHacked(studentRecord[1], studentRecord[2])) {
      let studentName = studentRecord[0];
      hackedNames.push(studentName);
    }
  }

  return hackedNames;
}

const output = findHack([
  ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
  ["name2", 120, ["B", "A", "A", "A"]],
  ["name3", 160, ["B", "A", "A", "A", "A"]],
  ["name4", 140, ["B", "A", "A", "C", "A"]],
]);
console.log(output);