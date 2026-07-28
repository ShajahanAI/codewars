// https://www.codewars.com/kata/5274e122fc75c0943d000148/train/javascript

// Passed

function groupByCommas(n) {
  let stringN = String(n);
  let result = "";
  for (let idx = stringN.length - 1; idx >= 0; idx--) {
    if (idx !== stringN.length - 1 && (stringN.length - idx) % 3 === 1) {
      result = "," + result;
    }

    result = stringN[idx] + result;
  }

  return result;
}

const output = groupByCommas(2147483647);
console.log(output);