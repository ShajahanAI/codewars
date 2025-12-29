// https://www.codewars.com/kata/5a023c426975981341000014/train/javascript

// Passed

function otherAngle(a, b) {
  let thirdAngle = 180 - (a + b);
  return thirdAngle;
}

const output = otherAngle(30, 60);
console.log(output);