// https://www.codewars.com/kata/63f96036b15a210058300ca9/train/javascript

// Passed

function secondSymbol(s, symbol) {
  let result = -1;
  let symbolCount = 0;
  for (let idx = 0; idx < s.length; idx++) {
    let char = s[idx];
    if (char === symbol) {
      if (symbolCount === 0) {
        symbolCount++;
        continue;
      }

      result = idx;
      break;
    }
  }

  return result;
}

const output = secondSymbol("Hello world!!!", "o");
console.log(output);