// https://www.codewars.com/kata/5b6c220fa0a661fbf200005d/train/javascript

// Passed

function scoreboard(string) {
  const scoreMap = {
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
    nil: 0,
  };

  const words = string.split(" ");
  const stringScores = words.slice(words.length - 2);
  const scores = stringScores.map((stringScore) =>
    Number(scoreMap[stringScore])
  );

  return scores;
}

const output = scoreboard("new score: two three");
console.log(output);