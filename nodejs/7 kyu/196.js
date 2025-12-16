// https://www.codewars.com/kata/52761ee4cffbc69732000738/train/javascript

// Passed

function goodVsEvil(good, evil) {
  let goodSide = [1, 2, 3, 3, 4, 10];
  let evilSide = [1, 2, 2, 2, 3, 5, 10];
  let goodSidePower = good
    .split(" ")
    .map((forceCount, forceIdx) => Number(forceCount) * goodSide[forceIdx])
    .reduce((prev, curr) => prev + curr, 0);
  let evilSidePower = evil
    .split(" ")
    .map((forceCount, forceIdx) => Number(forceCount) * evilSide[forceIdx])
    .reduce((prev, curr) => prev + curr, 0);
  let result;
  if (goodSidePower === evilSidePower) {
    result = "Battle Result: No victor on this battle field";
  } else {
    result =
      goodSidePower > evilSidePower
        ? "Battle Result: Good triumphs over Evil"
        : "Battle Result: Evil eradicates all trace of Good";
  }

  return result;
}

const output = goodVsEvil("0 0 0 0 0 10", "0 1 1 1 1 0 0");
console.log(output);