// https://www.codewars.com/kata/5a8bcd980025e99381000099/train/javascript

// Passed

function squareUp(n) {
  let result = [];
  for (let subArrNum = n; subArrNum > 0; subArrNum--) {
    let subArr = [];
    for (let elemNum = n; elemNum > 0; elemNum--) {
      if (elemNum >= subArrNum) {
        subArr.push(n - elemNum + 1);
      } else {
        subArr.push(0);
      }
    }

    result = result.concat(subArr.reverse());
  }

  return result;
}

const output = squareUp(4);
console.log(output);