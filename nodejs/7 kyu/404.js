// https://www.codewars.com/kata/62cecd4e5487c10028996e04/train/javascript

// Passed

function racePodium(blocks) {
  let secondPlace = Math.ceil(blocks / 3);
  let firstPlace = secondPlace + 1;
  let thirdPlace = blocks - firstPlace - secondPlace;

  if (thirdPlace === 0) {
    thirdPlace++;
    secondPlace--;
  }

  let result = [secondPlace, firstPlace, thirdPlace];
  return result;
}

const output = racePodium(10);
console.log(output);