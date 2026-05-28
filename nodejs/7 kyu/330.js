// https://www.codewars.com/kata/537baa6f8f4b300b5900106c/train/javascript

// Passed

function circleArea(radius) {
  if (radius <= 0) {
    throw new Error("radius has to be > 0");
  }
  let area = Math.PI * radius ** 2;
  return area;
}

const output = circleArea(68);
console.log(output);