// https://www.codewars.com/kata/594a1822a2db9e93bd0001d4/train/javascript

// Passed

function scratch(lottery) {
  const computeWinnings = (text) => {
    const words = text.split(" ");
    const animal = words[0];
    const won = words.slice(0, 3).every((word) => word === animal);
    return won ? Number(words[3]) : 0;
  };

  const winnings = lottery
    .map((text) => computeWinnings(text))
    .reduce((prev, curr) => prev + curr, 0);
  return winnings;
}

const output = scratch([
  "tiger tiger tiger 100",
  "rabbit dragon snake 100",
  "rat ox pig 1000",
  "dog cock sheep 10",
  "horse monkey rat 5",
  "dog dog dog 1000",
]);

console.log(output);