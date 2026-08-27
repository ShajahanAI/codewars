// https://www.codewars.com/kata/599da159a30addffd00000af/train/javascript

// Passed

function collision(x1, y1, radius1, x2, y2, radius2) {
  let getDistance = (x1, y1, x2, y2) =>
    ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5;
  let result = radius1 + radius2 >= getDistance(x1, y1, x2, y2);
  return result;
}

const output = collision(-1, 1, 10, -10.1, 1.1, 1);
console.log(output);