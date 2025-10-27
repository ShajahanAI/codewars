// https://www.codewars.com/kata/588463cae61257e44600006d/train/javascript

// Passed

function magicalWell(a, b, n) {
  let money = 0;
  for (let i = 0; i < n; i++) {
    money += a * b;
    a++;
    b++;
  }

  return money;
}

const output = magicalWell(6, 5, 3);
console.log(output);