// https://www.codewars.com/kata/580535462e7b330bd300003d/train/javascript

// Passed

function oracle(gestures) {
  let gestureToWinCountMap = new Object();
  let options = ["rock", "paper", "scissors"];

  let optionToPointDetailsMap = {
    rock: {
      rock: 0,
      paper: -1,
      scissors: 1,
    },

    paper: {
      rock: 1,
      paper: 0,
      scissors: -1,
    },
    scissors: {
      rock: -1,
      paper: 1,
      scissors: 0,
    },
  };

  let optionToTotalPoints = new Object();
  for (const option of options) {
    let totalPoints = 0;
    for (const gesture of gestures) {
      let pointsScored = optionToPointDetailsMap[option][gesture];
      totalPoints += pointsScored;
    }

    optionToTotalPoints[option] = totalPoints;
  }

  let totalPointsToOptions = new Object();
  options.map((option) => {
    let totalPoints = optionToTotalPoints[option];
    if (!(totalPoints in totalPointsToOptions)) {
      totalPointsToOptions[totalPoints] = [];
    }

    totalPointsToOptions[totalPoints].push(option);
  });

  let winningOptions = options.filter(
    (option) => optionToTotalPoints[option] > 0,
  );
  let result = winningOptions.length > 0 ? winningOptions.join("/") : "tie";
  return result;
}

const output = oracle(["paper", "scissors", "scissors"]);
console.log(output);