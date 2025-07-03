// https://www.codewars.com/kata/590adadea658017d90000039/train/javascript

// Passed

function fruit(reels, spins) {
  const itemValueMap = {
    Wild: 10,
    Star: 9,
    Bell: 8,
    Shell: 7,
    Seven: 6,
    Cherry: 5,
    Bar: 4,
    King: 3,
    Queen: 2,
    Jack: 1,
  };

  let scoreMultiplier = 1;
  const result = reels.map((reel, idx) => reel[spins[idx]]);
  const resultCountMap = new Object();
  for (const item of result) {
    if (!(item in resultCountMap)) {
      resultCountMap[item] = 0;
    }

    resultCountMap[item] += 1;
  }

  let totalScore = 0;
  for (const item of Object.keys(resultCountMap)) {
    let count = resultCountMap[item];
    if ((item === "Wild") & (count === 1)) {
      scoreMultiplier = 2;
    } else if (count == 3) {
      scoreMultiplier = 10;
    }

    totalScore += count === 1 ? 0 : itemValueMap[item];
  }

  let finalScore = scoreMultiplier * totalScore;
  return finalScore;
}

const output = fruit(
  [
    [
      "Wild",
      "Star",
      "Bell",
      "Shell",
      "Seven",
      "Cherry",
      "Bar",
      "King",
      "Queen",
      "Jack",
    ],
    [
      "Wild",
      "Star",
      "Bell",
      "Shell",
      "Seven",
      "Cherry",
      "Bar",
      "King",
      "Queen",
      "Jack",
    ],
    [
      "Wild",
      "Star",
      "Bell",
      "Shell",
      "Seven",
      "Cherry",
      "Bar",
      "King",
      "Queen",
      "Jack",
    ],
  ],
  [0, 4, 4]
);
console.log(output);