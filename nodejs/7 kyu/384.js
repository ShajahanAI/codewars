// https://www.codewars.com/kata/56971747aa359bdbf800004d/train/javascript

// Passed

function trickyDoubles(n) {
  let stringN = String(n);
  let isTrickyDouble =
    stringN.length % 2 === 0 &&
    stringN.slice(0, stringN.length / 2) === stringN.slice(stringN.length / 2);
  let result = isTrickyDouble ? n : n * 2;
  return result;
}

const output = trickyDoubles(4343);
console.log(output);