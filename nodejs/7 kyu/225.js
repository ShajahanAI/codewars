// https://www.codewars.com/kata/5734c38da41454b7f700106e/train/javascript

// Passed

function onlyOne(...args) {
  let trueCount = 0;
  for (let item of args) {
    if (item === true) {
      trueCount++;
    }

    if (trueCount > 1) {
      return false;
    }
  }

  if (trueCount === 0) {
    return false;
  }

  return true;
}

const output = onlyOne(true, false, false, true);
console.log(output);