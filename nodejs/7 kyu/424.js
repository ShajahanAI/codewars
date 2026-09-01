// https://www.codewars.com/kata/54fb963d3fe32351f2000102/train/javascript

// Passed

function collatz(n) {
  let result = 1;
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = n * 3 + 1;
    }
    result++;
  }

  return result;
}

const output = collatz(15);
console.log(output);
