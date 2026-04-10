// https://www.codewars.com/kata/65112af7056ad6004b5672f8/train/javascript

// Passed

function possiblyPerfect(key, answers) {
  let [correctAnswers, incorrectAnswers] = [0, 0];
  let result = true;
  for (let idx = 0; idx < key.length; idx++) {
    let studentAnswer = answers[idx];
    let correctAnswer = key[idx];

    if (correctAnswer === "_") {
      continue;
    }

    if (studentAnswer === correctAnswer) {
      correctAnswers++;
    } else {
      incorrectAnswers++;
    }

    if (correctAnswers > 0 && incorrectAnswers > 0) {
      result = false;
      break;
    }
  }

  return result;
}

const output = possiblyPerfect(
  ["A", "_", "C", "_", "B"],
  ["A", "D", "C", "E", "B"],
);
console.log(output);