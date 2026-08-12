// https://www.codewars.com/kata/59094c5d579da9aceb000037/train/javascript

// Passed

function increasingNumber(x, n) {
  for (let count = 1; count <= n; count++) {
    let remainder = x % count;
    if (remainder > 0) {
      x += count - remainder;
    }
  }

  return x;
}

const output = increasingNumber(9, 5, 15);
console.log(output);