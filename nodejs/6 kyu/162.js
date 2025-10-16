// https://www.codewars.com/kata/545f05676b42a0a195000d95/train/javascript

// Passed

function ranks(a) {
  let sortedArr = [...a].sort((a, b) => b - a); // sorts in descending order
  let numRankObject = new Object();
  let rank = 1;
  for (const num of sortedArr) {
    if (!(num in numRankObject)) {
      numRankObject[num] = rank;
    }
    rank++;
  }

  let rankArr = a.map((num) => numRankObject[num]);
  return rankArr;
}

const output = ranks([5, 2, 3, 5, 5, 4, 9, 8, 0]);
console.log(output);