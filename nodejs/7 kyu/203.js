// https://www.codewars.com/kata/58846b46f4456a8919000025/train/javascript

// Passed

function appleBoxes(k) {
  let redApples = 0;
  let yellowApples = 0;
  for (let i = 1; i <= k; i++) {
    if (i % 2 === 0) {
      redApples += i ** 2;
    } else {
      yellowApples += i ** 2;
    }
  }

  let difference = redApples - yellowApples;
  return difference;
}

const output = appleBoxes(5);
console.log(output);