// https://www.codewars.com/kata/5da9973d06119a000e604cb6/train/javascript

// Passed

function countingValleys(s) {
  let [result, currentLevel] = [0, 0];
  let enteredValley = false;
  for (const direction of s) {
    if (direction === "F") {
      continue;
    } else if (direction === "U") {
      currentLevel++;
    } else if (direction === "D") {
      currentLevel--;
    }

    if (currentLevel < 0) {
      enteredValley = true;
    } else if (currentLevel >= 0 && enteredValley) {
      enteredValley = false; // exited valley
      result++;
    }
  }

  return result;
}

const output = countingValleys("UFFDDFDUDFUFU");
console.log(output);