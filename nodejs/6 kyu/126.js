// https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/javascript

// Passed

function bouncingBall(h, bounce, window) {
  if (h <= 0 || bounce <= 0 || bounce >= 1 || window >= h) return -1;
  let viewCount = 1; // mother will see the ball when it is falling

  while (h * bounce > window) {
    viewCount += 2; // mother will see it 2 times (when it bounces and falls back)
    h *= bounce;
  }

  return viewCount;
}

const output = bouncingBall(30.0, 0.66, 1.5);
console.log(output);