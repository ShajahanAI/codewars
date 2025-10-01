// https://www.codewars.com/kata/5a39724945ddce2223000800/train/javascript

// Passed

function totalAmountVisible(topNum, numOfSides) {
  let oppositeNum = numOfSides + 1 - topNum;
  let totalVisibleNums = 0;
  for (let currentNum = 1; currentNum <= numOfSides; currentNum++) {
    if (currentNum === oppositeNum) continue;
    totalVisibleNums += currentNum;
  }

  return totalVisibleNums;
}

const output = totalAmountVisible(3, 6);
console.log(output);