// https://www.codewars.com/kata/53222010db0eea35ad000001/train/javascript

// Passed

function getSlope(p1, p2) {
  let [x1, y1] = p1;
  let [x2, y2] = p2;
  let slope = x1 - x2 === 0 ? null : (y1 - y2) / (x1 - x2);
  return slope;
}

const output = getSlope([5, 3], [8, 9]);
console.log(output);