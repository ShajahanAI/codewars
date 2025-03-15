// https://www.codewars.com/kata/58de08d376f875dbb40000f1/train/javascript

// Passed

function premierLeagueStandings(teamStandings) {
  let newStandings = { 1: teamStandings[1] };
  Object.values(teamStandings)
    .filter((team) => team !== teamStandings[1])
    .sort()
    .forEach((team, idx) => {
      newStandings[idx + 2] = team;
    });
  return newStandings;
}

const output = premierLeagueStandings({
  2: "Arsenal",
  3: "Accrington Stanley",
  1: "Leeds United",
});
console.log(output);