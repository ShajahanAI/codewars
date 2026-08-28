// https://www.codewars.com/kata/59377c53e66267c8f6000027/train/javascript

// Passed

function alphabetWar(fight) {
  let leftSide = {
    w: 4,
    p: 3,
    b: 2,
    s: 1,
  };

  let rightSide = {
    m: 4,
    q: 3,
    d: 2,
    z: 1,
  };

  let [leftSideSum, rightSideSum] = [0, 0];
  for (const letter of fight) {
    if (letter in leftSide) {
      leftSideSum += leftSide[letter];
    } else if (letter in rightSide) {
      rightSideSum += rightSide[letter];
    }
  }

  let result;
  if (leftSideSum === rightSideSum) {
    result = "Let's fight again!";
  } else if (leftSideSum > rightSideSum) {
    result = "Left side wins!";
  } else {
    result = "Right side wins!";
  }

  return result;
}

const output = alphabetWar("zdqmwpbs");
console.log(output);