// https://www.codewars.com/kata/52ed326b8df6540e06000029/train/javascript

// Passed

function goto(level, button) {
  // type cleansing
  if (typeof level !== "number") {
    return 0; // invalid level
  }

  if (typeof button !== "string") {
    return 0; // invalid button
  }

  button = Number(button);
  const validLevels = [0, 1, 2, 3];
  if (!validLevels.includes(level) | !validLevels.includes(button)) {
    return 0; // received invalid floor
  }

  return button - level;
}

const output = goto(1, '3');
console.log(output);