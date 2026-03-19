// https://www.codewars.com/kata/57613fb1033d766171000d60/train/javascript

// Passed

function uefaEuro2016(teams, scores) {
  let [team1, team2] = teams;
  let [team1Score, team2Score] = scores;
  let result = `At match ${team1} - ${team2}, `;

  if (team1Score == team2Score) {
    result += "teams played draw.";
  } else {
    if (team1Score > team2Score) {
      result += `${team1} won!`;
    } else {
      result += `${team2} won!`;
    }
  }

  return result;
}

const output = uefaEuro2016(["Belgium", "Italy"], [0, 2]);
console.log(output);