// https://www.codewars.com/kata/588e27b7d1140d31cb000060/train/javascript

// Passed

function generatePairs(n) {
  let pairsArray = [];
  for (let a = 0; a <= n; a++) {
    for (let b = a; b <= n; b++) {
      let pair = [a, b];
      pairsArray.push(pair);
    }
  }

  return pairsArray;
}

const output = generatePairs(2);
console.log(output);