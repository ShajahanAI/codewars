// https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/javascript

// Passed

function thirt(n) {
  let patternNumbers = [1, 10, 9, 12, 3, 4];
  let digitsReversed = String(n).split("").reverse();
  let currentStationaryNumber = 0;
  let prevStationaryNumber;
  while (currentStationaryNumber !== prevStationaryNumber) {
    prevStationaryNumber = currentStationaryNumber;
    currentStationaryNumber = 0;
    for (let idx = 0; idx < digitsReversed.length; idx++) {
      let digit = digitsReversed[idx];
      let patternNumber = patternNumbers[idx % 6];
      currentStationaryNumber += digit * Number(patternNumber);
    }

    digitsReversed = String(currentStationaryNumber).split("").reverse();
  }

  return currentStationaryNumber;
}

const output = thirt(8529);
console.log(output);