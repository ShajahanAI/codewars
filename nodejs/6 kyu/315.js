// https://www.codewars.com/kata/58417e9ab9c25c774500001f/train/javascript

// Passed

function missingAngle(h, a, o) {
  let inverseFunction, theta;
  if (o && h) {
    inverseFunction = Math.asin;
    theta = o / h;
  } else if (a && h) {
    inverseFunction = Math.acos;
    theta = a / h;
  } else {
    inverseFunction = Math.atan;
    theta = o / a;
  }

  let thetaInRadians = inverseFunction(theta);
  let thetaInDegrees = (thetaInRadians * 180) / Math.PI;
  return thetaInDegrees;
}

const output = missingAngle(8, 0, 5);
console.log(output);