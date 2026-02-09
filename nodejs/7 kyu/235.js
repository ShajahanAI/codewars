// https://www.codewars.com/kata/5868812b15f0057e05000001/train/javascript

// Passed

function tailSwap(arr) {
  let [x, y] = arr;
  let xSplit = x.split(":");
  let ySplit = y.split(":");
  let [modifiedX, modifiedY] = [
    xSplit[0] + ":" + ySplit[1],
    ySplit[0] + ":" + xSplit[1],
  ];
  let modifiedArr = [modifiedX, modifiedY];
  return modifiedArr;
}

const output = tailSwap(["abc:123", "cde:456"], ["abc:456", "cde:123"]);
console.log(output);