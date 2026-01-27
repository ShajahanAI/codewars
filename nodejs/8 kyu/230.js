// https://www.codewars.com/kata/5bb904724c47249b10000131/train/javascript

// Passed

function points(games) {
  let totalPoints = 0;
  for (const game of games) {
    let [ourScore, opponentScore] = game
      .split(":")
      .map((score) => Number(score));
    if (ourScore > opponentScore) {
      totalPoints += 3;
    } else if (ourScore === opponentScore) {
      totalPoints++;
    }
  }

  return totalPoints;
}

const output = points([
  "1:0",
  "2:0",
  "3:0",
  "4:0",
  "2:1",
  "3:1",
  "4:1",
  "3:2",
  "4:2",
  "4:3",
]);
console.log(output);