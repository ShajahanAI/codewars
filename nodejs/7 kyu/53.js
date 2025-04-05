// https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/javascript

// Passed

function checkExam(array1, array2) {
  const scores = array2.map((submitted_answer, idx) => {
    if (submitted_answer.trim().length === 0) {
      // Blank answer
      return 0;
    }

    return submitted_answer === array1[idx] ? 4 : -1;
  });

  let totalScore = Math.max(
    scores.reduce((prev, curr) => prev + curr, 0),
    0
  ); // prevents -ve score

  // Returning total score
  return totalScore;
}

const output = checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]);
console.log(output);
