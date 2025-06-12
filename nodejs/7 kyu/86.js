// https://www.codewars.com/kata/5840946ea3d4c78e90000068/train/javascript

// Passed

function gameWinners(gryffindor, slytherin) {
  const calculateScore = (teamResult) =>
    teamResult[0] + (teamResult[1] === "yes" ? 150 : 0);
  const gryffindorScore = calculateScore(gryffindor);
  const slytherinScore = calculateScore(slytherin);

  if (gryffindorScore == slytherinScore) return "It's a draw!";
  return gryffindorScore > slytherinScore
    ? "Gryffindor wins!"
    : "Slytherin wins!";
}

const output = gameWinners([100, "yes"], [100, "no"]);
console.log(output);