// https://www.codewars.com/kata/58da7ae9b340a2440500009c/train/javascript

// Passed

function pointInCircle(x, y) {
  let result = x ** 2 + y ** 2 < 1; // formula of circle is x**2 + y**2 = r**2 (r is radius)
  return result;
}

const output = pointInCircle(0.5, 0.5);
console.log(output);