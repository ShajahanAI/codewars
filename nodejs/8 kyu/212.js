// https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/javascript

// Passed

function monkeyCount(n) {
  let numberArr = [];
  for (let num = 1; num < n + 1; num++) {
    numberArr.push(num);
  }

  return numberArr;
}

const output = monkeyCount(10);
console.log(output);