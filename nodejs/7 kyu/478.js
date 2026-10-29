// https://www.codewars.com/kata/5797bbb34be9127074000132/train/javascript

// Passed

function tetration(x, y) {
  let result = 1;
  if (y === 0) {
    return result;
  }

  for (let i = 0; i < y; i++) {
    result = x ** result;
  }

  return result;
}

const output = tetration(5, 2);
console.log(output);